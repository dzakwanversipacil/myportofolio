import datetime
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.db.models import F
from django.core import serializers
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, JsonResponse
from django.utils.http import url_has_allowed_host_and_scheme
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from main.forms import ExperienceForm, EducationForm, ProjectForm
from main.models import Experience, Education, Project

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Dzakwan Farabi Al Muzhaffar",
        "npm": "2506612436",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Undergraduate student at the Faculty of Computer Science."
            "Actively engaged in coursework related to information systems"
            "architecture, programming, and data science."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)

def show_experience(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Dzakwan Farabi Al Muzhaffar",
        "title_query": title_query,
        "form": ExperienceForm(),
    }
    return render(request, "experience.html", context)

def show_education(request):
    organization_query = request.GET.get("organization", "").strip()

    context = {
        "name": "Dzakwan Farabi Al Muzhaffar",
        "organization_query": organization_query,
        "form": EducationForm(),
    }
    return render(request, "education.html", context)

def show_project(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Dzakwan Farabi Al Muzhaffar",
        "title_query": title_query,
        "form": ProjectForm(),
    }
    return render(request, "project.html", context)

@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.has_perm('main.add_experience'):
        raise PermissionDenied

    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience added successfully!")
        return redirect("main:show_experience")

    context = {
        "name": "Dzakwan Farabi Al Muzhaffar",
        "form": form,
    }
    return render(request, "experience_form.html", context)

@login_required(login_url="/login/")
def create_education(request):
    if not request.user.has_perm('main.add_education'):
        raise PermissionDenied

    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Education added successfully!")
        return redirect("main:show_education")

    context = {
        "name": "Dzakwan Farabi Al Muzhaffar",
        "form": form,
    }
    return render(request, "education_form.html", context)

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.has_perm('main.add_project'):
        raise PermissionDenied

    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Project added successfully!")
        return redirect("main:show_project")

    context = {
        "name": "Dzakwan Farabi Al Muzhaffar",
        "form": form,
    }
    return render(request, "project_form.html", context)

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.prefetch_related('loved_by').all().order_by(F('end_date').desc(nulls_first=True), '-start_date')

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    data = []
    for experience in experiences:
        loved_users = experience.loved_by.all()
        is_loved = request.user in loved_users if request.user.is_authenticated else False
        loved_by_names = ", ".join([u.username for u in loved_users])

        data.append({
            "pk": str(experience.id),
            "fields": {
                "title": experience.title,
                "description": experience.description,
                "organization": experience.organization,
                "formatted_year": experience.formatted_year,
                "image_url": experience.image_url,
                "love_count": loved_users.count(),
                "is_loved": is_loved,
                "loved_by_names": loved_by_names,
            }
        })

    return JsonResponse(data, safe=False)

def get_education_json(request):
    organization_query = request.GET.get("organization", "").strip()
    educations = Education.objects.prefetch_related('starred_by').all().order_by(F('end_date').asc(nulls_last=True), 'start_date')

    if organization_query:
        educations = educations.filter(organization__icontains=organization_query)

    data = []
    for education in educations:
        starred_users = education.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(education.id),
            "fields": {
                "description": education.description,
                "organization": education.organization,
                "field_of_study": education.field_of_study,
                "formatted_year": education.formatted_year,
                "image_url": education.image_url,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

def get_project_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.prefetch_related('starred_by').all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "tech_stack": project.tech_stack,
                "project_url": project.project_url,
                "project_image_url": project.project_image_url,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.has_perm('main.delete_experience'):
        raise PermissionDenied
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience Deleted Successfully!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

@login_required(login_url="/login/")
def delete_education(request, education_id):
    if not request.user.has_perm('main.delete_education'):
        raise PermissionDenied

    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Education Deleted Successfully!")
        return redirect("main:show_education")

    return redirect("main:show_education")

@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.has_perm('main.delete_project'):
        raise PermissionDenied

    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project Deleted Successfully!")
        return redirect("main:show_project")

    return redirect("main:show_project")

@login_required(login_url="/login/")
def update_experience(request, experience_id):
    if not request.user.has_perm('main.change_experience'):
        raise PermissionDenied
    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience updated successfully!")
        return redirect("main:show_experience")

    context = {
        "name": "Dzakwan Farabi Al Muzhaffar",
        "form": form,
    }
    return render(request, "experience_form.html", context)

@login_required(login_url="/login/")
def update_education(request, education_id):
    if not request.user.has_perm('main.change_education'):
        raise PermissionDenied

    education = get_object_or_404(Education, pk=education_id)
    form = EducationForm(request.POST or None, instance=education)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Education updated successfully!")
        return redirect("main:show_education")

    context = {
        "name": "Dzakwan Farabi Al Muzhaffar",
        "form": form,
    }
    return render(request, "education_form.html", context)

@login_required(login_url="/login/")
def update_project(request, project_id):
    if not request.user.has_perm('main.change_project'):
        raise PermissionDenied

    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Project updated successfully!")
        return redirect("main:show_project")

    context = {
        "name": "Dzakwan Farabi Al Muzhaffar",
        "form": form,
    }
    return render(request, "project_form.html", context)

@require_POST
def create_experience_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Only the portfolio owner can add experiences."},
            status=403,
        )

    form = ExperienceForm(request.POST)
    if form.is_valid():
        experience = form.save()
        return JsonResponse(
            {"message": "Experience successfully added.", "pk": str(experience.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

@require_POST
def create_education_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Only the portfolio owner can add educations."},
            status=403,
        )

    form = EducationForm(request.POST)
    if form.is_valid():
        education = form.save()
        return JsonResponse(
            {"message": "Education successfully added.", "pk": str(education.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Only the portfolio owner can add projects."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "Project successfully added.", "pk": str(project.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Dzakwan Farabi Al Muzhaffar",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)

        next_url = request.POST.get('next') or request.GET.get('next') or '/'

        if not url_has_allowed_host_and_scheme(url=next_url, allowed_hosts={request.get_host()}):
            next_url = '/'

        response = redirect(next_url)
        response.set_cookie("last_login", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Dzakwan Farabi Al Muzhaffar",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/login/")
def toggle_love(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        if request.user in experience.loved_by.all():
            experience.loved_by.remove(request.user)
        else:
            experience.loved_by.add(request.user)

    return redirect("main:show_experience")

@login_required(login_url="/login/")
def toggle_star(request, section_type, section_id):

    model_mapping = {
        "experience": Experience,
        "education": Education,
        "project": Project,
    }

    if section_type not in model_mapping:
        return redirect("main:show_main")

    SectionModel = model_mapping[section_type]
    
    item = get_object_or_404(SectionModel, pk=section_id)

    if request.method == "POST":
        if request.user in item.starred_by.all():
            item.starred_by.remove(request.user)
        else:
            item.starred_by.add(request.user)

    return redirect(f"main:show_{section_type}")
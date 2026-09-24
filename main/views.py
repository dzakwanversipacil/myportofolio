from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
from django.db.models import F
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.forms import ExperienceForm, EducationForm
from main.models import Experience, Education

def show_main(request):
    context = {
        "name": "Dzakwan Farabi Al Muzhaffar",
        "npm": "2506612436",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Undergraduate student at the Faculty of Computer Science."
            "Actively engaged in coursework related to information systems"
            "architecture, programming, and data science."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    json_response = get_experience_json(request)

    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )

    experiences = [experience.object for experience in experiences]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Dzakwan Farabi Al Muzhaffar",
        "experience_list": experiences,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)

def show_education(request):
    json_response = get_education_json(request)
    
    educations = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )

    educations = [education.object for education in educations]
    organization_query = request.GET.get("organization", "").strip()

    context = {
        "name": "Dzakwan Farabi Al Muzhaffar",
        "education_list": educations,
        "organization_query": organization_query,
    }
    return render(request, "education.html", context)

def create_experience(request):
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

def create_education(request):
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

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all().order_by(F('end_date').desc(nulls_first=True), '-start_date')

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    experiences_json = serializers.serialize("json", experiences)
    return HttpResponse(experiences_json, content_type="application/json")

def get_education_json(request):
    organization_query = request.GET.get("organization", "").strip()
    educations = Education.objects.all().order_by(F('end_date').asc(nulls_last=True), 'start_date')

    if organization_query:
        educations = educations.filter(organization__icontains=organization_query)

    educations_json = serializers.serialize("json", educations)
    return HttpResponse(educations_json, content_type="application/json")

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience Deleted Successfully!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Education Deleted Successfully!")
        return redirect("main:show_education")

    return redirect("main:show_education")

def update_experience(request, experience_id):
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

def update_education(request, education_id):
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
        login(request, form.get_user())
        return redirect("main:show_main")

    context = {
        "name": "Dzakwan Farabi Al Muzhaffar",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    return redirect("main:show_main")
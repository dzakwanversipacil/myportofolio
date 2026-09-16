from django.shortcuts import render
from django.db.models import F
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.forms import ExperienceForm
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
    educations = Education.objects.all().order_by(F('end_date').asc(nulls_last=True), 'start_date')
    
    context = {
        "name": "Dzakwan Farabi Al Muzhaffar",
        "education_list": educations,
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

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all().order_by(F('end_date').desc(nulls_first=True), '-start_date')

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    experiences_json = serializers.serialize("json", experiences)
    return HttpResponse(experiences_json, content_type="application/json")

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience Deleted Successfully!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")
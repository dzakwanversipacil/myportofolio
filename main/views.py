from django.shortcuts import render
from django.db.models import F
from main.models import Experience


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
    experiences = Experience.objects.all().order_by(F('end_date').desc(nulls_first=True), '-start_date')
    
    context = {
        "name": "Dzakwan Farabi Al Muzhaffar",
        "experience_list": experiences,
    }
    return render(request, "experience.html", context)
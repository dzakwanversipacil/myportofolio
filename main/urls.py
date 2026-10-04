from django.urls import path

from main.views import *

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("education/", show_education, name="show_education"),
    path("project/", show_project, name="show_project"),

    path("experience/add/", create_experience, name="create_experience"),
    path("education/add/", create_education, name="create_education"),
    path("project/add/", create_project, name="create_project"),

    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("api/education/", get_education_json, name="get_education_json"),
    path("api/project/", get_project_json, name="get_project_json"),

    path("experience/<uuid:experience_id>/delete/",delete_experience,name="delete_experience"),
    path("education/<uuid:education_id>/delete/",delete_education,name="delete_education"),
    path("project/<uuid:project_id>/delete/",delete_project,name="delete_project"),

    path("experience/<uuid:experience_id>/update/", update_experience, name="update_experience"),
    path("education/<uuid:education_id>/update/", update_education, name="update_education"),
    path("project/<uuid:project_id>/update/", update_project, name="update_project"),

    path("experience/add-ajax/", create_experience_ajax, name="create_experience_ajax"),
    path("project/add-ajax/", create_project_ajax, name="create_project_ajax"),

    path("experience/<uuid:experience_id>/love/", toggle_love, name="toggle_love"),
    path("<str:section_type>/<uuid:section_id>/star/", toggle_star, name="toggle_star"),

    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
]
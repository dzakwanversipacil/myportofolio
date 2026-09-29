from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, URLInput

from main.models import Experience, Education, Project

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "organization",
            "start_date",
            "end_date",
            "image_url",
        ]

        labels = {
            "title": "Experience Title",
            "description": "Experience Description",
            "organization": "Organization",
            "start_date": "Start Date",
            "end_date": "End Date",
            "image_url": "Image URL",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "ex. Data Scientist Intern",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "ex. Worked on data analysis and machine learning projects.",
                    "rows": 3,
                }
            ),
            "organization": TextInput(
                            attrs={
                                "placeholder": "ex. Google",
                                "maxlength": 255,
                            }
                        ),
            "start_date": DateTimeInput(
                attrs={
                    "placeholder": "ex. 2023-01-01 09:00:00",
                }
            ),
            "end_date": DateTimeInput(
                attrs={
                    "placeholder": "ex. 2023-06-30 17:00:00",
                }
            ),
            "image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=<FILE_ID>&sz=w1000",
                }
            ),
        }

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "description",
            "organization",
            "field_of_study",
            "start_date",
            "end_date",
            "image_url",
        ]

        labels = {
            "description": "Education Description",
            "organization": "Education Institution",
            "field_of_study": "Field of Study",
            "start_date": "Start Date",
            "end_date": "End Date",
            "image_url": "Image URL",
        }

        widgets = {
            "description": Textarea(
                attrs={
                    "placeholder": "ex. Worked on data analysis and machine learning projects.",
                    "rows": 3,
                }
            ),
            "organization": TextInput(
                            attrs={
                                "placeholder": "ex. Google",
                                "maxlength": 255,
                            }
                        ),
            "field_of_study": TextInput(
                            attrs={
                                "placeholder": "ex. Information Systems",
                                "maxlength": 255,
                            }
                        ),
            "start_date": DateTimeInput(
                attrs={
                    "placeholder": "ex. 2023-01-01 09:00:00",
                }
            ),
            "end_date": DateTimeInput(
                attrs={
                    "placeholder": "ex. 2023-06-30 17:00:00",
                }
            ),
            "image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=<FILE_ID>&sz=w1000",
                }
            ),
        }

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tech_stack": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }
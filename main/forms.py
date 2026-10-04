from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, URLInput
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

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

        def clean_organization(self):
                    organization = strip_tags(self.cleaned_data["organization"]).strip()
                    if not organization:
                        raise ValidationError("Nama organisasi tidak boleh hanya berisi tag HTML.")
                    return organization
        
        def clean_field_of_study(self):
            return strip_tags(self.cleaned_data["field_of_study"]).strip()

        def clean_description(self):
            return strip_tags(self.cleaned_data["description"]).strip()

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
            "title": "Project Name",
            "description": "Project Description",
            "tech_stack": "Tech Stack",
            "project_url": "Project URL",
            "project_image_url": "Project Image URL",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "ex. Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "ex. A website used to display my background as an Information Systems Student.",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "ex. Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "ex. https://github.com/dzakwanversipacil/myportofolio",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=<FILE_ID>&sz=w1000",
                }
            ),
        }

        def clean_title(self):
            title = strip_tags(self.cleaned_data["title"]).strip()
            if not title:
                raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML.")
            return title

        def clean_tech_stack(self):
            return strip_tags(self.cleaned_data["tech_stack"]).strip()

        def clean_description(self):
            return strip_tags(self.cleaned_data["description"]).strip()
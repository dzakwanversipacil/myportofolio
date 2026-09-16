from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, URLInput

from main.models import Experience

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
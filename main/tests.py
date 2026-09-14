from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from main.models import Experience, Education

class MainTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        
        self.assertContains(response, "Dzakwan Farabi Al Muzhaffar")
        self.assertContains(response, "2506612436")
        self.assertContains(response, "S1 Sistem Informasi")
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")
        self.assertEqual(response.status_code, 404)


class ExperienceTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            organization="Fasilkom UI",
            description="Membantu mahasiswa memahami pengembangan web.",
            start_date=timezone.now(),
        )

    def test_experience_model_str(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")

    def test_experience_page_accessible_and_correct_template(self):
        response = self.client.get(reverse("main:show_experience"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")

    def test_experience_data_appears_in_html(self):
        response = self.client.get(reverse("main:show_experience"))
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.organization)
        self.assertContains(response, self.experience.description)

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))
        self.assertContains(response, "Belum ada data pengalaman.")


class EducationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.education = Education.objects.create(
            organization="Universitas Indonesia",
            field_of_study="Sistem Informasi",
            description="Mempelajari arsitektur sistem informasi dan pemrograman.",
            start_date=timezone.now(),
        )

    def test_education_model_str(self):
        self.assertEqual(str(self.education), "Universitas Indonesia")

    def test_education_url_is_accessible_and_uses_correct_template(self):
        response = self.client.get(reverse("main:show_education"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "education.html")

    def test_education_data_appears_in_html_when_data_exists(self):
        response = self.client.get(reverse("main:show_education"))
        self.assertContains(response, self.education.organization)
        self.assertContains(response, self.education.field_of_study)

    def test_education_html_displays_empty_message_when_no_data(self):
        Education.objects.all().delete()
        response = self.client.get(reverse("main:show_education"))
        self.assertContains(response, "Belum ada data pendidikan.")
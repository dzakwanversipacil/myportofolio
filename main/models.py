import uuid
from django.db import models

class Experience(models.Model):
    """
        Sementara Experience Section tidak memiliki kategori, 
        namun jika ingin menambahkan kategori, nanti bisa di-uncomment
        EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]"""
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    organization = models.CharField(max_length=255, default='')
    start_date = models.DateTimeField(blank=True, null=True) 
    end_date = models.DateTimeField(blank=True, null=True)
    image_url = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title
        
    @property
    def is_ongoing(self):
        return self.ended_at is None

    @property
    def formatted_year(self):
        if not self.start_date:
            return ""
        
        start_year = self.start_date.strftime("%Y")
        
        if self.end_date:
            end_year = self.end_date.strftime("%Y")
            if start_year == end_year:
                return start_year
            return f"{start_year} - {end_year}"
        
        return f"{start_year} - Present"

class Education(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    organization = models.CharField(max_length=255, default='')
    field_of_study = models.CharField(max_length=255, default='')
    start_date = models.DateTimeField(blank=True, null=True) 
    end_date = models.DateTimeField(blank=True, null=True)
    image_url = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title
        
    @property
    def is_ongoing(self):
        return self.ended_at is None

    @property
    def formatted_year(self):
        if not self.start_date:
            return ""
        
        start_year = self.start_date.strftime("%Y")
        
        if self.end_date:
            end_year = self.end_date.strftime("%Y")
            if start_year == end_year:
                return start_year
            return f"{start_year} - {end_year}"
        
        return f"{start_year} - Present"
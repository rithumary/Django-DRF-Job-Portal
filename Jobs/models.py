from django.db import models

# Create your models here.
class CompanyDb(models.Model):
    company_name=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    industry=models.CharField(max_length=200)
    website=models.URLField()
    contact_email=models.EmailField()

    def __str__(self):
        return self.company_name

class JobDb(models.Model):
    job_title=models.CharField(max_length=200)
    company = models.ForeignKey(
        'CompanyDb',
        on_delete=models.CASCADE,
        related_name='jobs'
    )
    description=models.TextField()
    required_skills=models.CharField(max_length=200)
    salary=models.PositiveIntegerField()
    experience_required=models.PositiveIntegerField()
    job_type=models.CharField(max_length=200)
    is_active=models.BooleanField(default=True)
    posted_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job_title

class ApplicationDb(models.Model):
    applicant_name=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.CharField(max_length=200)
    job = models.ForeignKey(
        'JobDb',
        on_delete=models.CASCADE,
        related_name='applications'
    )
    qualification=models.CharField(max_length=200)
    experience=models.PositiveIntegerField(default=0)
    cover_letter=models.TextField()
    status=models.CharField(max_length=200,default='pending')
    applied_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.applicant_name



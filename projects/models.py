from django.db import models
from django.core.validators import FileExtensionValidator

class Project(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=500)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    logo = models.ImageField(upload_to='project_logos/', default='default_logo.png')
    team_member = models.ForeignKey(
        'Our_Team',
        on_delete=models.CASCADE,
        related_name='projects',
        default=None,
    )

    class Meta:
        verbose_name = 'Project'

    def __str__(self):
        return self.title


class Our_Team(models.Model):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)
    achievements = models.CharField(max_length=500, blank=True, null=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='about_us_images/')
    resume = models.FileField(
        upload_to='about_us_resumes/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
        default=None
    )
    content = models.TextField()

    class Meta:
        verbose_name = 'Our_Team'
        verbose_name_plural = 'Our_Team'

    def __str__(self):
        return f"{self.username} - {self.first_name} {self.last_name}"


class WorkExperience(models.Model):
    team_member = models.ForeignKey(
        Our_Team,
        on_delete=models.CASCADE,
        related_name="work_experiences"
    )
    logo = models.ImageField(upload_to='work_experience_logos/', blank=True, null=True)
    company_name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)  # null means Present

    def __str__(self):
        if self.end_date:
            return f"{self.company_name} ({self.start_date} - {self.end_date})"
        return f"{self.company_name} ({self.start_date} - Present)"


class Image(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)

    def __str__(self):
        return f"Image for {self.project.title}"

class PersonalImage(models.Model):
    image = models.ImageField(upload_to='project_images',blank=True,null=True)

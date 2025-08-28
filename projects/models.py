from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=500)
    content = RichTextField()  # ✅ Rich text instead of TextField
    date = models.DateField(auto_now_add=True)

    verbose_name = 'Project'
    def __str__(self):
        return self.title

class Image(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='project_images/',blank=True, null=True)
    video = models.FileField(upload_to='project_videos/',blank=True, null=True)
    verbose_name = 'Project Image'

class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='about_us_images/')
    content = RichTextField()
    verbose_name = 'About Us'

    def __str__(self):
        return self.title
    
class Home(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    verbose_name = 'Home'

    def __str__(self):
        return self.title
    
class HomeImage(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='home_images')
    image = models.ImageField(upload_to='home_images/')
    verbose_name = 'Home Image'
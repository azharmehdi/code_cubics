from django.contrib import admin
from .models import Project, Image, Our_Team, WorkExperience

# Project + multiple images
class ImageInline(admin.TabularInline):
    model = Image
    extra = 3  
    fields = ['image']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'excerpt', 'date']
    search_fields = ['title', 'excerpt']
    inlines = [ImageInline]


# Work Experience inline for Our_Team
class WorkExperienceInline(admin.TabularInline):
    model = WorkExperience
    extra = 1  # how many blank rows you want by default
    fields = ['company_name', 'designation', 'start_date', 'end_date', 'logo']


# Our_Team with WorkExperience
class Our_TeamAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'title', 'expertise']
    search_fields = ['username', 'first_name', 'last_name', 'title']
    inlines = [WorkExperienceInline]


# Register models
admin.site.register(Project, ProjectAdmin)
admin.site.register(Our_Team, Our_TeamAdmin)

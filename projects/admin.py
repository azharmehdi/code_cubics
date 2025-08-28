from django.contrib import admin
from .models import Project, Image, Home, HomeImage, AboutUs

# Project + multiple images

class ImageInline(admin.TabularInline):
    model = Image
    extra = 3  
    fields = ['image', 'video']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'excerpt', 'date']
    search_fields = ['title', 'excerpt']
    inlines = [ImageInline]

admin.site.register(Project, ProjectAdmin)

# Home + multiple images

class HomeImageInline(admin.TabularInline):
    model = HomeImage
    fields = ['image']

class HomeAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    search_fields = ['title', 'description']
    inlines = [HomeImageInline]

admin.site.register(Home, HomeAdmin)

# AboutUs (single image)

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']

admin.site.register(AboutUs, AboutUsAdmin)

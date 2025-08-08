from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectListAPI.as_view(), name='index'),  # example route
    path('about/', views.Our_TeamListAPI.as_view(), name='about'),
    path('api/process-text/', views.process_text, name='process_text'),
]

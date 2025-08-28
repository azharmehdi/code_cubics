from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectListAPI.as_view(), name='index'),  # example route
    path('about/', views.AboutUsListAPI.as_view(), name='about'),
    path('home/', views.HomeListAPI.as_view(), name='home'),
    
]

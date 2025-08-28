from rest_framework import generics
from .models import Project, AboutUs, Home
from .serializers import ProjectSerializer, AboutUsSerializer, HomeSerializer

# Read-only API views
class ProjectListAPI(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class AboutUsListAPI(generics.ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

class HomeListAPI(generics.ListAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer

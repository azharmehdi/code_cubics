from rest_framework import serializers
from .models import Project, Image, Our_Team, WorkExperience, SignUp

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image']

class ProjectSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)  # include related images

    class Meta:
        model = Project
        fields = ['id', 'title', 'excerpt', 'content', 'date', 'images', 'logo']


class ProjectMiniSerializer(serializers.ModelSerializer):
    """Lightweight project serializer for showing under team profile"""
    class Meta:
        model = Project
        fields = ['id', 'title', 'excerpt','date']  # only basic info for team page

class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = ['id', 'logo', 'company_name', 'designation', 'start_date', 'end_date']
        
class Our_TeamSerializer(serializers.ModelSerializer):
    projects = ProjectMiniSerializer(many=True, read_only=True)  # nested projects
    work_experiences = WorkExperienceSerializer(many=True, read_only=True)  # nested work experiences

    class Meta:
        model = Our_Team
        fields = [
            'id', 'username', 'first_name', 'last_name',
            'expertise', 'achievements', 'title', 'image',
            'resume', 'content', 'projects', 'work_experiences'
        ]




class TextProcessSerializer(serializers.Serializer):
    text = serializers.CharField()

class SignUpSerializer(serializers.Serializer):
    text=serializers.CharField()
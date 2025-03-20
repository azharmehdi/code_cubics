from rest_framework import generics
from .models import Project, Our_Team
from .serializers import ProjectSerializer, Our_TeamSerializer, TextProcessSerializer,SignUpSerializer
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from utils.text_processor import process_text_rules

# List all projects (full details)
class ProjectListAPI(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# Retrieve a single project by ID (full details)
class ProjectDetailAPI(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'id'

# List all team members (with nested mini projects)
class Our_TeamListAPI(generics.ListAPIView):
    queryset = Our_Team.objects.all()
    serializer_class = Our_TeamSerializer

# Retrieve a single team member by ID (with their projects)
class Our_TeamDetailAPI(generics.RetrieveAPIView):
    queryset = Our_Team.objects.all()
    serializer_class = Our_TeamSerializer
    lookup_field = 'id'

@api_view(['POST'])
def process_text(request):
    serializer = TextProcessSerializer(data=request.data)
    if serializer.is_valid():
        text = serializer.validated_data['text']
        # Split lines for multi-line support
        lines = text.splitlines()
        processed_lines = [process_text_rules(line) for line in lines]
        processed_text = '\n'.join(processed_lines)
        return Response({'processed_text': processed_text})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
def validate_data(request):
    serializer=SignUpSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
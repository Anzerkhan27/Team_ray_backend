from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet # type: ignore
from .models import Project, Member
from .serializers import ProjectSerializer, MemberSerializer

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_serializer_context(self):
        return {'request': self.request}
    
class MemberViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def get_serializer_context(self):
        return {'request': self.request}
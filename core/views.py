from django.shortcuts import render # type: ignore
from rest_framework.viewsets import ModelViewSet # type: ignore
from rest_framework import viewsets # type: ignore
from .models import Project, Member, Contact, Post
from .serializers import ProjectSerializer, MemberSerializer, ContactSerializer, PostSerializer

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
    


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer



class PostViewSet(ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')  # Fetch latest first
    serializer_class = PostSerializer

    def get_serializer_context(self):
        return {'request': self.request}

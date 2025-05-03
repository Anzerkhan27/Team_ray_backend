from rest_framework import serializers # type: ignore
from .models import Project, Member, Contact, Post, PostImage

class ProjectSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'image', 'created_at']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None

class MemberSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Member
        fields = ['id', 'name', 'role', 'bio', 'image']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

    

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['image']  # Serialize the 'image' field of PostImage

class PostSerializer(serializers.ModelSerializer):
    images = PostImageSerializer(many=True, read_only=True)  # Include related images

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'post_type', 'created_at', 'images']  # Return images as a list
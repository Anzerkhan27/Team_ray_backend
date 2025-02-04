from django.db import models



class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/', null=True, blank=True)  # Image fieldpyt
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='team_members/', null=True, blank=True)

    def __str__(self):
        return self.name

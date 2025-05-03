from django.db import models # type: ignore



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



class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name




class Post(models.Model):
    TITLE_MAX_LENGTH = 200

    NEWS = 'news'
    EVENT = 'event'
    ANNOUNCEMENT = 'announcement'

    POST_TYPES = [
        (NEWS, 'News'),
        (EVENT, 'Event'),
        (ANNOUNCEMENT, 'Announcement'),
    ]

    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    content = models.TextField()
    post_type = models.CharField(max_length=20, choices=POST_TYPES, default=NEWS)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news_images/')
    
    def __str__(self):
        return f"Image for {self.post.title}"

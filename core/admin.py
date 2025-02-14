from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Project, Member, Contact, Post

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')  # Fields to display in the admin list view


admin.site.register(Member)
admin.site.register(Contact)
admin.site.register(Post)
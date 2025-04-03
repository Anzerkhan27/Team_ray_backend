# Register your models here.
from django.contrib import admin # type: ignore
from .models import Project, Member, Contact, Post, PostImage


class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1  # Number of empty forms to show initially

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_type', 'created_at')  # Fields to display in the admin list view
    inlines = [PostImageInline]



@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')  # Fields to display in the admin list view


admin.site.register(Member)
admin.site.register(Contact)



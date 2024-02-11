from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'email']
    list_per_page = 20

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ['title', 'tagline']
    list_per_page = 20

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'category', 'status']
    list_editable = ['status', 'category']
    list_per_page = 20

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['blog', 'name', 'comment', 'active', 'date']
    list_editable = ['active']
    list_per_page = 20

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'date']
    list_per_page = 20

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['title', 'note', 'date', 'seen']
    list_per_page = 20

admin.site.register(BlogCategory)
admin.site.register(Tag)
admin.site.register(Log)

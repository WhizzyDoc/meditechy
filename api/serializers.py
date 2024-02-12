from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class AdminSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Admin
        fields = ['id', 'user', 'first_name', 'last_name', 'email', 'api_token', 'image']

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ['title', 'tagline', 'about', 'logo', 'icon', 'image', 'email',
                  'phone', 'address', 'github', 'linkedin', 'twitter', 'facebook',
                  'instagram']

class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ['id', 'title']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']

class BlogSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer(many=False, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    class Meta:
        model = Blog
        fields = ['id', 'title', 'author', 'category', 'post', 'image', 'thumbnail',
                  'allow_comments', 'tags', 'status', 'keywords', 'description',
                  'created', 'comments']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'name', 'comment', 'reply', 'active', 'date']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'subject', 'message', 'reply', 'date']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'title', 'note', 'date', 'seen']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'title', 'note', 'date', 'seen']

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ['id', 'action', 'date']


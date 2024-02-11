from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from tinymce.models import HTMLField
from PIL import Image

# Create your models here.
class Site(models.Model):
    title = models.CharField(max_length=250, blank=True)
    tagline = models.CharField(max_length=250, blank=True)
    about = HTMLField(blank=True)
    logo = models.ImageField(upload_to="site/images/", blank=True)
    icon = models.ImageField(upload_to="site/images/", blank=True)
    image = models.ImageField(upload_to="site/images/", blank=True)
    email = models.EmailField(max_length=200, blank=True)
    phone = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=1000, blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    def __str__(self):
        return f'{self.title}'
    def save(self, *args, **kwargs):
        super(Site, self).save(*args, **kwargs)
        if self.icon:
            img = Image.open(self.icon.path)
            target_w = 100
            target_h = 100
            img_sized = img.resize((target_w, target_h), Image.ANTIALIAS)
            img_sized.save(self.icon.path)

class Admin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="admin")
    first_name = models.CharField(max_length=100, verbose_name="First Name", null=True)
    last_name = models.CharField(max_length=100, verbose_name="Last Name", null=True)
    email = models.EmailField(max_length=200, blank=True)
    api_token = models.CharField(max_length=250, verbose_name="API Key", blank=True)
    image = models.ImageField(upload_to="admin/images/", blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def save(self, *args, **kwargs):
        super(Admin, self).save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            target_w = 200
            target_h = 200
            img_sized = img.resize((target_w, target_h), Image.ANTIALIAS)
            img_sized.save(self.image.path)

    class Meta:
        ordering = ['first_name']


class BlogCategory(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['title']
    
class Blog(models.Model):
    author = models.CharField(max_length=250, null=True, blank=True)
    title = models.CharField(max_length=250, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, related_name="blogs", null=True, blank=True)
    post = HTMLField(null=True, blank=True)
    image = models.ImageField(upload_to="blogs/images/", null=True, blank=True)
    thumbnail = models.ImageField(upload_to="blogs/thumbnails/", null=True, blank=True)
    allow_comments = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name="blogs")
    status = models.CharField(max_length=100, default="Published", choices=(("Draft", "Draft"),("Published", "Published")))
    keywords = models.CharField(max_length=2000, null=True, blank=True)
    comments = models.PositiveIntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    def save(self, *args, **kwargs):
        super(Blog, self).save(*args, **kwargs)
        if self.thumbnail:
            img = Image.open(self.thumbnail.path)
            target_w = 340
            target_h = 200
            img_sized = img.resize((target_w, target_h), Image.ANTIALIAS)
            img_sized.save(self.thumbnail.path)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created']
    
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="blog_comments", null=True)
    name = models.CharField(max_length=150)
    comment = models.TextField()
    reply = HTMLField(null=True, blank=True)
    active = models.BooleanField(default=True)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.comment
    class Meta:
        ordering = ['date']

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=256)
    message = models.TextField()
    reply = HTMLField(blank=True)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.message
    class Meta:
        ordering = ['-date']

class Notification(models.Model):
    title = models.CharField(max_length=150)
    note = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    seen = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-date']

class Log(models.Model):
    action = models.CharField(max_length=2000)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.action
    class Meta:
        ordering = ['-date']

# Generated by Django 4.1.4 on 2024-02-09 10:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=250, null=True)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('post', tinymce.models.HTMLField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blogs/images/')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='blogs/thumbnails/')),
                ('allow_comments', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Published', 'Published')], default='Published', max_length=100)),
                ('keywords', models.CharField(blank=True, max_length=2000, null=True)),
                ('comments', models.PositiveIntegerField(default=0)),
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('subject', models.CharField(max_length=256)),
                ('message', models.TextField()),
                ('reply', tinymce.models.HTMLField(blank=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=2000)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('note', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('seen', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250)),
                ('tagline', models.CharField(blank=True, max_length=250)),
                ('about', tinymce.models.HTMLField(blank=True)),
                ('logo', models.ImageField(blank=True, upload_to='site/images/')),
                ('icon', models.ImageField(blank=True, upload_to='site/images/')),
                ('image', models.ImageField(blank=True, upload_to='site/images/')),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('phone', models.CharField(blank=True, max_length=200)),
                ('address', models.CharField(blank=True, max_length=1000)),
                ('github', models.URLField(blank=True)),
                ('linkedin', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
                ('facebook', models.URLField(blank=True)),
                ('instagram', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('comment', models.TextField()),
                ('reply', tinymce.models.HTMLField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_comments', to='api.blog')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blogs', to='api.blogcategory'),
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='blogs', to='api.tag'),
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=100, null=True, verbose_name='Last Name')),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('api_token', models.CharField(blank=True, max_length=250, verbose_name='API Key')),
                ('image', models.ImageField(blank=True, upload_to='admin/images/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['first_name'],
            },
        ),
    ]
# Generated by Django 4.1.3 on 2023-01-28 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('body', models.TextField()),
                ('createdd', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_blog_posts', to=settings.AUTH_USER_MODEL)),
                ('tag', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
        migrations.CreateModel(
            name='Commnt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('body', models.TextField(max_length=500)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
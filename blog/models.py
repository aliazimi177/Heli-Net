from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


# Create your models here.
class Post(models.Model):
    STATUS = (("draft", "Draft"), ("published", "Published"))
    CATEGORY = (
        ("programming", "Programming"),
        ("game", "game"),
        ("network", "network"),
        ("linux", "linux"),
        ("android", "android"),
        ("graphic", "graphic"),
    )

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="author_blog_posts"
    )
    title = models.CharField(max_length=250, null=False)
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    publish = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    createdd = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS, default="draft")
    image = models.ImageField(upload_to="static/uploads/%Y-%m-%d %H:%M:%S", default="")
    tag = TaggableManager()
    category = models.CharField(max_length=50, default="", choices=CATEGORY)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.slug])

    class Meta:
        ordering = ("-publish",)


class Commnt(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=50)
    body = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    email = models.EmailField(max_length=254, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name} commented {self.post}"

    class Meta:
        ordering = ("created",)

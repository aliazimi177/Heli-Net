from django.shortcuts import render,get_object_or_404
from blog.models import Post
from blog.forms import *
from taggit.models import Tag
def index(request,tag_slug=None):
    posts = Post.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag,slug=tag_slug)
        posts = posts.filter(tag__in=[tag])

    post = Post.objects.last()
    tag = None
    context = {"post":post,"posts":posts,"tag":tag}
    return render(request,"blog/helinet_index.html",context)


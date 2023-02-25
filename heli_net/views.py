from django.shortcuts import render,get_object_or_404
from blog.models import Post
from blog.forms import *
from taggit.models import Tag
from django.contrib.postgres.search import SearchVector
def index(request,tag_slug=None):
    posts = Post.objects.all()[:6]
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag,slug=tag_slug)
        posts = posts.filter(tag__in=[tag])

    post = Post.objects.last()
    tag = None
    context = {"post":post,"posts":posts,"tag":tag}
    return render(request,"blog/helinet_index.html",context)

def search(request):
    query = request.GET.get('q')
    out_comes = []
    form = SearchForm()
    if 'query' in request.GET:
        form  = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
    out_comes = Post.objects.annotate(search=SearchVector('title','body')).filter(search=query)

    

    context = {'form':form,'query':query,'out_comes':out_comes}
    return render(request,"blog/search.html",context)


def about_us(request):
    return render(request, "blog/about_us.html")













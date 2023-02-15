from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from blog.models import Post, Commnt
from django.http import HttpResponse
from taggit.models import Tag
from django.core.mail import send_mail

# Create your views here.
def post_detail(request, post):
    posts = Post.objects.all()
    post = get_object_or_404(Post, slug=post, status="published")
    tags = Post.tag.all()
    comments = Commnt.objects.all()
    comment = Commnt.objects.filter(active=True)
    comment_form = CommentForm(request.POST or None)
    if request.method == "POST":
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return HttpResponse(request.path_info)
        else:
            comment_form = CommentForm()
    return render(
        request,
        "blog/post_detail.html",
        {
            "tags": tags,
            "post": post,
            "comment": comment,
            "forms": comment_form,
            "comment": comment,
            "comment": comment,
        },
    )
def post_share(request,post_id):
    post = get_object_or_404(Post,id=post_id,status="published")
    form = EmailPostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            cd  = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recomment you"
            message = f"{post.title} in {post_url} just have look"
            send_mail(
                subject,message,"Hellinet177@gmail.com",
                [cd['to'],],
            )
        else:
            form = EmailPostForm()
    context = {'post':post,'form':form,}
    return render(request,"blog/share.html",context)


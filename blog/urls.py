from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "blog"
urlpatterns = [
    path("<slug:post>/", views.post_detail, name="post_detail"),
    path("<int:post_id>/share/",views.post_share,name="post_share"),
]

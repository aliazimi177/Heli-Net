from django.contrib import admin
from .models import *
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title","author","status",)
    search_fields = ("title","slug")
    list_editable = ("status",)
    list_filter = ("status",)
@admin.register(Commnt)
class CommntAdmin(admin.ModelAdmin):
    list_display=("name",)
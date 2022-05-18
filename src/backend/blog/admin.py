from django.contrib import admin
from blog.models import Tag, Post, Comment

# Register your models here.

# Tagの登録
admin.site.register(Tag)
# Postの登録
admin.site.register(Post)
# Commentの登録
admin.site.register(Comment)
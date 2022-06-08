import os
from django.contrib import admin
from blog.models import Tag, Post, Comment
from django.utils.safestring import mark_safe

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    """記事投稿用画面"""
    list_display = ['title', 'showImage']

    def showImage(self, obj):
        return mark_safe('<img src="{}" style="width:200px; height:auto;">'.format(obj.image.url))


# Tagの登録
admin.site.register(Tag)
# Postの登録
admin.site.register(Post, PostAdmin)
# Commentの登録
admin.site.register(Comment)
import os
from django.contrib import admin
from blog.models import Tag, Category, Post, Comment
from django.utils.safestring import mark_safe

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    """記事投稿用画面"""
    # 表示項目
    list_display = ['title', 'showImage', 'created_at']
    # 検索欄
    search_fields = ['title']
    # 日付ナビゲーション
    date_hierarchy = 'created_at'
    
    fieldsets = [
        ('タイトル情報', {'fields' : ['title', 'subtitle']}),
        ('記事', {'fields' : ['body', 'meta_description', 'image']}),
        ('タグ・カテゴリー設定', {'fields' : ['category', 'tags']}),
        ('作成者', {'fields': ['author']})
    ]

    def showImage(self, obj):
        if obj.image:
            return mark_safe('<img src="{}" style="width:100px; height:auto;">'.format(obj.image.url))
        return


# Tagの登録
admin.site.register(Tag)
# Categoryの登録
admin.site.register(Category)
# Postの登録
admin.site.register(Post, PostAdmin)
# Commentの登録
admin.site.register(Comment)
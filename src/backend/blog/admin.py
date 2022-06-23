from django.contrib import admin
from django.utils.safestring import mark_safe
from markdownx.admin import MarkdownxModelAdmin

from blog.models.tag import Tag
from blog.models.category import Category
from blog.models.post import Post
from blog.models.comment import Comment

from treenode.admin import TreeNodeModelAdmin
from treenode.forms import TreeNodeForm

# Register your models here.

class PostAdmin(MarkdownxModelAdmin):
    """記事投稿・編集用画面"""
    # 表示項目
    list_display = ['title', 'showImage', 'created_at']
    # 検索欄
    search_fields = ['title']
    # 日付ナビゲーション
    date_hierarchy = 'created_at'
    
    fieldsets = [
        ('タイトル情報', {'fields' : ['title']}),
        ('記事', {'fields' : ['body', 'meta_description', 'image']}),
        ('タグ・カテゴリー設定', {'fields' : ['category', 'tags']}),
        ('作成者', {'fields': ['author']})
    ]

    def showImage(self, obj):
        if obj.image:
            return mark_safe('<img src="{}" style="width:100px; height:auto;">'.format(obj.image.url))
        return
        
class TagAdmin(admin.ModelAdmin):
    """タグ追加・編集用画面"""
    # 表示項目
    list_display = ['name', 'created_at']
    
    fieldsets = [
        ('タグ名', {'fields' : ['name']}),
    ]

class CategoryAdmin(TreeNodeModelAdmin):
    """カテゴリー追加・編集用画面"""
    # 一覧表示スタイル
    treenode_display_mode = TreeNodeModelAdmin.TREENODE_DISPLAY_MODE_ACCORDION
    # treenode_display_mode = TreeNodeModelAdmin.TREENODE_DISPLAY_MODE_BREADCRUMBS
    # treenode_display_mode = TreeNodeModelAdmin.TREENODE_DISPLAY_MODE_INDENTATION
    
    form = TreeNodeForm

class CommentAdmin(TreeNodeModelAdmin):
    """コメント追加・編集用画面"""
    # 一覧表示スタイル
    treenode_display_mode = TreeNodeModelAdmin.TREENODE_DISPLAY_MODE_ACCORDION
    # treenode_display_mode = TreeNodeModelAdmin.TREENODE_DISPLAY_MODE_BREADCRUMBS
    # treenode_display_mode = TreeNodeModelAdmin.TREENODE_DISPLAY_MODE_INDENTATION
    
    form = TreeNodeForm



# Tagの登録
admin.site.register(Tag, TagAdmin)
# Categoryの登録
admin.site.register(Category, CategoryAdmin)
# Postの登録
admin.site.register(Post, PostAdmin)
# Commentの登録
admin.site.register(Comment, CommentAdmin)
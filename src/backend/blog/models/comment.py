import uuid
from django.db import models
from treenode.models import TreeNodeModel

from .post import Post

class Comment(TreeNodeModel):
    """コメント"""
    treenode_display_field = 'text'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('名前', max_length=255, default='名無し')
    text = models.TextField('本文')
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, verbose_name='対象記事')
    created_at = models.DateTimeField('作成日', auto_now_add=True)
    updated_at = models.DateTimeField('修正日', auto_now=True)

    class Meta(TreeNodeModel.Meta):
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
    
    def __str__(self):
        return self.text[:20]
    
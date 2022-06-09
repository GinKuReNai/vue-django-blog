import uuid
from django.db import models

from .post import Post

class Comment(models.Model):
    """コメント"""
    class Meta:
        # 作成日、修正日で降順に並べる
        ordering = ['-created_at', '-updated_at']
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('名前', max_length=255, default='名無し')
    text = models.TextField('本文')
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, verbose_name='対象記事')
    parent = models.ForeignKey('self', related_name='replies', verbose_name='親コメント', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField('作成日', auto_now_add=True)
    updated_at = models.DateTimeField('修正日', auto_now=True)
    
    def __str__(self):
        return self.text[:20]
    
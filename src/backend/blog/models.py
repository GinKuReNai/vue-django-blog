from django.db import models
from user.models import Profile

# Create your models here.

class Tag(models.Model):
    """記事のタグ"""
    name = models.CharField('タグ', max_length=25, unique=True)
    
    class Meta:
        verbose_name_plural = 'tags'
    
    def __str__(self):
        return self.name

class Post(models.Model):
    """記事"""
    class Meta:
        ordering = ['-publish_date']
    
    title = models.CharField('タイトル', max_length=255, unique=True)
    subtitle = models.CharField('サブタイトル', max_length=255, blank=True)
    slug = models.SlugField('識別番号', max_length=255, unique=True)
    body = models.TextField('本文')
    meta_description = models.CharField('メタ情報', max_length=150, blank=True)
    date_created = models.DateTimeField('作成日時', auto_now_add=True)
    date_modified = models.DateTimeField('修正日時', auto_now=True)
    publish_date = models.DateTimeField('投稿日時', blank=True, null=True)
    published = models.BooleanField('公開日時', default=False)
    
    author = models.ForeignKey(Profile, related_name='posts', on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, related_name='tags', blank=True)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    """コメント"""
    name = models.CharField('名前', max_length=255, default='名無し')
    text = models.TextField('本文')
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, verbose_name='対象記事')
    parent = models.ForeignKey('self', related_name='replies', verbose_name='親コメント', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField('作成日', auto_now_add=True)
    
    def __str__(self):
        return self.text[:20]
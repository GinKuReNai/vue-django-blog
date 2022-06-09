import uuid
from django.utils import timezone
from django.db import models
from django.dispatch import receiver
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.utils.text import slugify

User = get_user_model()

class Tag(models.Model):
    """記事のタグ"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('タグ', max_length=25, unique=True)
    created_at = models.DateTimeField('作成日', auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'tags'
    
    def __str__(self):
        return self.name

class Category(models.Model):
    """記事のカテゴリー"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('カテゴリー', max_length=25, unique=True)
    created_at = models.DateTimeField('作成日', auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name

class Post(models.Model):
    """記事"""
    class Meta:
        # 投稿日時で降順に並べる
        ordering = ['-created_at', '-updated_at']
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField('タイトル', max_length=255, unique=True)
    subtitle = models.CharField('サブタイトル', max_length=255, blank=True)
    slug = models.SlugField('slug', unique=True)
    body = models.TextField('本文')
    meta_description = models.CharField('メタ情報', max_length=150, blank=True)
    image = models.ImageField(upload_to='posts', blank=True, null=True)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('修正日時', auto_now=True)
    
    author = models.ForeignKey(User, related_name='posts', on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(Category, verbose_name='カテゴリー', related_name='category', on_delete=models.PROTECT, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def get_api_url(self):
        """URLの設定"""
        try:
            return reverse('posts_api:detail_post', kwargs={'slug': self.slug})
        except:
            None


def create_slug(instance, new_slug=None):
    """slugの自動生成"""
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    
    qs = Post.objects.filter(slug=slug).order_by('-id')
    # 同じ名前のslugが1つでも存在する場合
    if qs.exists():
        new_slug = '%s-%s' % (slug, qs.first().id)
        # -idを付け加えたslugをもとに再起処理
        return create_slug(instance, new_slug=new_slug)
    
    return slug

@receiver(pre_save, sender=Post)
def pre_save_post_receiver(sender, instance, *args, **kwargs):
    """Postの保存前処理"""
    if not instance.slug:
        instance.slug = create_slug(instance)


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
    
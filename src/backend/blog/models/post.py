import uuid
from django.db import models
from django.dispatch import receiver
from django.shortcuts import reverse
from django.db.models.signals import pre_save
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from markdownx.models import MarkdownxField

from .tag import Tag
from .category import Category

User = get_user_model()


def postsImage_directory_path(instance, filename):
    """画像名をUUIDに変更して保存"""
    return 'posts/{}.{}'.format(str(uuid.uuid4()), filename.split('.')[-1])


class Post(models.Model):
    """記事"""
    class Meta:
        # 投稿日時で降順に並べる
        ordering = ['-created_at', '-updated_at']
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField('タイトル', max_length=255, unique=True)
    slug = models.SlugField('slug', unique=True)
    body = MarkdownxField('本文')     # Markdown Text
    meta_description = models.CharField('メタ情報', max_length=150, blank=True)
    image = models.ImageField(upload_to=postsImage_directory_path, blank=True, null=True)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('修正日時', auto_now=True)
    
    author = models.ForeignKey(User, related_name='posts', on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    category = models.ForeignKey(Category, to_field='slug', verbose_name='カテゴリー', related_name='category', on_delete=models.PROTECT, null=True, blank=True)
    
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

import uuid
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.text import slugify

class Category(models.Model):
    """記事のカテゴリー"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('カテゴリー', max_length=25, unique=True)
    slug = models.SlugField('slug', unique=True)
    created_at = models.DateTimeField('作成日', auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name

def create_slug(instance, new_slug=None):
    """slugの自動生成"""
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    
    qs = Category.objects.filter(slug=slug).order_by('-id')
    # 同じ名前のslugが1つでも存在する場合
    if qs.exists():
        new_slug = '%s-%s' % (slug, qs.first().id)
        # -idを付け加えたslugをもとに再起処理
        return create_slug(instance, new_slug=new_slug)
    
    return slug

@receiver(pre_save, sender=Category)
def pre_save_post_receiver(sender, instance, *args, **kwargs):
    """Categoryの保存前処理"""
    if not instance.slug:
        instance.slug = create_slug(instance)

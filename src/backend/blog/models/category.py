import uuid
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.text import slugify

class Category(models.Model):
    """記事のカテゴリー"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('カテゴリー', max_length=25, unique=True)
    created_at = models.DateTimeField('作成日', auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name

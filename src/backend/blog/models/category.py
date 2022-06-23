import uuid
from django.db import models
from treenode.models import TreeNodeModel

class Category(TreeNodeModel):
    """記事のカテゴリー"""
    treenode_display_field = 'name' 

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('カテゴリー', max_length=25, unique=True)
    created_at = models.DateTimeField('作成日', auto_now_add=True)
    
    class Meta(TreeNodeModel.Meta):
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

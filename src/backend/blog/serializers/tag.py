from rest_framework import serializers
from blog.models import Tag

class TagSerializer(serializers.ModelSerializer):
    """Profile用シリアライザ"""
    class Meta:
        model = Tag
        # 利用するモデルのフィールド
        fields = ['name']
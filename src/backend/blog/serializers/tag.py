from rest_framework import serializers
from blog.models import Tag

class TagPrimaryKeyRelatedSerializer(serializers.PrimaryKeyRelatedField, serializers.ModelSerializer):
    """ManyToMany登録用シリアライザ"""
    class Meta:
        model = Tag
        # 利用するモデルのフィールド
        fields = ['name']

class TagListSerializer(serializers.ModelSerializer):
    """Tag一覧シリアライザ"""
    class Meta:
        model = Tag
        fields = ['id', 'name', 'created_at']

class TagCreateUpdateSerializer(serializers.ModelSerializer):
    """Tag追加・更新シリアライザ"""
    class Meta:
        model = Tag
        fields = ['name', 'created_at']
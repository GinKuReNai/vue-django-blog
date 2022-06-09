from rest_framework import serializers
from blog.models.category import Category

class CategoryListSerializer(serializers.ModelSerializer):
    """Category一覧シリアライザ"""
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at']

class CategoryCreateUpdateSerializer(serializers.ModelSerializer):
    """Category追加・更新シリアライザ"""
    class Meta:
        model = Category
        fields = ['name', 'created_at']
from rest_framework import serializers
from blog.models.category import Category

class CategoryListSerializer(serializers.ModelSerializer):
    """Category一覧シリアライザ"""
    class Meta:
        model = Category
        # fields = ['id', 'parent', 'name', 'created_at']
        fields = '__all__'

class CategoryCreateUpdateSerializer(serializers.ModelSerializer):
    """Category追加・更新シリアライザ"""
    class Meta:
        model = Category
        fields = ['name', 'created_at']
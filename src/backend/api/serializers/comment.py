from rest_framework import serializers
from blog.model import Comment

class CommentSerializer(serializers.ModelSerializer):
    """コメントシリアライザ"""
    class Meta:
        model = Comment
        fields = [
            'id',
            'text',
            'post',
            'parent',
            'created_at',
            'updated_at',
        ]

class CommentCreateSerializer(serializers.ModelSerializer):
    """作成時シリアライザ"""
    class Meta:
        model = Comment
        fields = [
            'text'
        ]
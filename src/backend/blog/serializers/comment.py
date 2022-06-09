from rest_framework import serializers
from blog.models.comment import Comment

class CommentSerializer(serializers.ModelSerializer):
    """コメントシリアライザ"""
    class Meta:
        model = Comment
        fields = [
            'id',
            'name',
            'text',
            'post',
            'parent',
            'created_at',
            'updated_at',
        ]

class CommentCreateUpdateSerializer(serializers.ModelSerializer):
    """作成時シリアライザ"""
    class Meta:
        model = Comment
        fields = ['name', 'text']
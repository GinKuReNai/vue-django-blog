from rest_framework import serializers
from user.models import Tag

class TagSerializer(serializers.ModelSerializer):
    """Profile用シリアライザ"""
    class Meta:
        model = Profile
        # 利用するモデルのフィールド
        fields = ['name']
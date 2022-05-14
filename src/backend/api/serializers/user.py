from rest_framework import serializers
from django.contrib.auth import get_user_model
from user.models import Profile

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """User用シリアライザ"""
    # ManyToOne関係のPost
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        # 利用するモデルのフィールド
        fields = ['username', 'nickname', 'email', 'date_of_birth', 'posts']

class ProfileSerializer(serializers.ModelSerializer):
    """Profile用シリアライザ"""
    class Meta:
        model = Profile
        # 利用するモデルのフィールド
        fields = ['website', 'twitter', 'github', 'bio']


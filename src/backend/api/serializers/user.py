from rest_framework import serializers

from user.models import User, Profile

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


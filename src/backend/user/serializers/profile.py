from rest_framework import serializers
from user.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    """Profile用シリアライザ"""
    class Meta:
        model = Profile
        # 利用するモデルのフィールド
        fields = ['website', 'twitter', 'github', 'bio', 'thumbnail', 'background']
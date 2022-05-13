from rest_framework import generics
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from api.serializers.user import ProfileSerializer
from user.models import Profile
from api.permissions import IsOwner

class ProfileListAPIView(generics.ListAPIView):
    """Profile用取得（一覧）API"""
    # 認証(Login)ユーザーのみ利用可
    perimission_classes = [IsAuthenticated,]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Profile用詳細取得・更新・削除API"""
    # 認証(Login)ユーザー / ReadOnly / 本人のみ利用可
    perimission_classes = [IsAuthenticatedOrReadOnly, IsOwner]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileCreateAPIView(generics.CreateAPIView):
    """Profile用登録API"""
    # 誰でも利用可
    perimission_classes = [AllowAny,]
    serializer_class = ProfileSerializer

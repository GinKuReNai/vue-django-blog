from rest_framework import generics
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from user.serializers.user import UserSerializer
from user.models import User
from blog.components.permissions import IsOwner

class UserListAPIView(generics.ListAPIView):
    """User用取得（一覧）API"""
    # 認証(Login)ユーザーのみ利用可
    perimission_classes = [IsAuthenticated,]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """User用詳細取得・更新・削除API"""
    # 認証(Login)ユーザー / ReadOnly / 本人のみ利用可
    perimission_classes = [IsAuthenticatedOrReadOnly, IsOwner]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

class UserCreateAPIView(generics.CreateAPIView):
    """User用登録API"""
    # 誰でも利用可
    perimission_classes = [AllowAny,]
    serializer_class = UserSerializer

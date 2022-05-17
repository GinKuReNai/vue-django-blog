from rest_framework import generics
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from blog.serializers.tag import TagSerializer
from blog.models import Tag
from blog.components.permissions import IsOwner, IsOwnerOrReadOnly

class TagListAPIView(generics.ListAPIView):
    """Tag用取得（一覧）API"""
    # 認証(Login)ユーザーのみ利用可
    perimission_classes = [IsAuthenticated,]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Tag用詳細取得・更新・削除API"""
    # 認証(Login)ユーザー / ReadOnly / 本人のみ利用可
    perimission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'id'

class TagCreateAPIView(generics.CreateAPIView):
    """Tag用登録API"""
    # 認証(Login)ユーザー / 本人のみ利用可
    perimission_classes = [IsAuthenticatedOrReadOnly,]
    serializer_class = TagSerializer

from rest_framework import generics
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticatedOrReadOnly,
)
from blog.serializers import tag
from blog.models.tag import Tag
from blog.components.permissions import IsOwnerOrReadOnly

class TagListAPIView(generics.ListAPIView):
    """Tag用取得（一覧）API"""
    # 認証(Login)ユーザーのみ利用可
    perimission_classes = [AllowAny,]
    queryset = Tag.objects.all()
    serializer_class = tag.TagListSerializer

class TagDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Tag用詳細取得・更新・削除API"""
    # 認証(Login)ユーザー / ReadOnly / 本人のみ利用可
    perimission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Tag.objects.all()
    serializer_class = tag.TagCreateUpdateSerializer
    lookup_field = 'name'

class TagCreateAPIView(generics.CreateAPIView):
    """Tag用登録API"""
    # 認証(Login)ユーザー / 本人のみ利用可
    perimission_classes = [IsAuthenticatedOrReadOnly,]
    serializer_class = tag.TagCreateUpdateSerializer

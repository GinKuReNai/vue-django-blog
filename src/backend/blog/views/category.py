from rest_framework import generics
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticatedOrReadOnly,
)
from blog.serializers import category
from blog.models import Category
from blog.components.permissions import IsOwnerOrReadOnly

class CategoryListAPIView(generics.ListAPIView):
    """Category用取得（一覧）API"""
    # 認証(Login)ユーザーのみ利用可
    perimission_classes = [AllowAny,]
    queryset = Category.objects.all()
    serializer_class = category.CategoryListSerializer

class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Category用詳細取得・更新・削除API"""
    # 認証(Login)ユーザー / ReadOnly / 本人のみ利用可
    perimission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = category.CategoryCreateUpdateSerializer
    lookup_field = 'id'

class CategoryCreateAPIView(generics.CreateAPIView):
    """Category用登録API"""
    # 認証(Login)ユーザー / 本人のみ利用可
    perimission_classes = [IsAuthenticatedOrReadOnly,]
    serializer_class = category.CategoryCreateUpdateSerializer

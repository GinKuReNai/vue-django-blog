from rest_framework import generics
from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from blog.serializers.post import (
    PostCreateUpdateSerializer,
    PostDetailSerializer,
    PostListSerializer,
)
from blog.models.post import Post
from blog.components.permissions import IsOwnerOrReadOnly
from blog.components.pagination import PostPageNumberPagination

class PostListAPIView(generics.ListAPIView):
    """Post用取得（一覧）API"""
    # 認証(Login)ユーザー / Read Only のみ利用可
    perimission_classes = [IsAuthenticatedOrReadOnly,]
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    # Paginationを設定
    pagination_class = PostPageNumberPagination
    
class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Post用詳細取得・更新・削除API"""
    # 認証(Login)ユーザー / ReadOnly / 本人のみ利用可
    perimission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'

class PostCreateAPIView(views.APIView):
    """Post用登録API"""
    # 認証(Login)ユーザーのみ利用可
    perimission_classes = [IsAuthenticated,]
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer

    def post(self, request, *args, **kwargs):
        """登録時処理（userをauthorとして登録）"""
        serializer = PostCreateUpdateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save(author=request.user)
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response({'errors': serializer.errors}, status=404)


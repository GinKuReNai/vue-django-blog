from rest_framework import generics
from rest_framework import views
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from django.shotcuts import get_object_or_404
from api.serializers.blog import CommentSerializer
from blog.models import Comment
from api.permissions import IsOwner, IsOwnerOrReadOnly
from api.mixin import MultipleFieldLookupMixin

class CommentListAPIView(views.APIView):
    """Comment用取得（一覧）API"""
    # 認証(Login)ユーザー / Read Only のみ利用可
    perimission_classes = [IsAuthenticatedOrReadOnly,]
    
    def get(self, request, slug):
        """取得時処理(slugを対象としたコメントの取得)"""
        post = Post.objects.get(slug=slug)
        comments = Comment.objects.filter(post=post)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=200)
    
class CommentDetailAPIView(
    MultipleFieldLookupMixin,
    RetrieveUpdateDestroyAPIView
):
    """
    Comment用詳細取得・更新・削除API
    
    MultipleFieldLookupMixinを多重継承して複数のCommentを取得
    """
    # 認証(Login)ユーザー / ReadOnly / 本人のみ利用可
    perimission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_fields = ['post', 'id']

class CommentCreateAPIView(views.APIView):
    """Comment用登録API"""
    # 認証(Login)ユーザーのみ利用可
    perimission_classes = [IsAuthenticated,]
    serializer_class = CommentSerializer

    def post(self, request, *args, **kwargs):
        """登録時処理（Userをauthor, Postをpostとして登録）"""
        post = get_object_or_404(Post, slug=slug)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user, post=post)
            return Response(serializer.data, status=200)
        else:
            return Response({'errors': serializer.errors}, status=400)
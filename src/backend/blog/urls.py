from django.urls import path, include
from blog.views import tag, post, comment

app_name = 'blog'

urlpatterns = [
  path('', post.PostListAPIView.as_view(), name='list_post'),
  path('create/', post.PostCreateAPIView.as_view(), name='create_post'),
  path('<str:slug>/', post.PostDetailAPIView.as_view(), name='detail_post'),
  path('<str:slug>/comment/', comment.CommentListAPIView.as_view(), name='list_comment'),
  path('<str:slug>/comment/create/', comment.CommentCreateAPIView.as_view(), name='create_comment'),
  path('<str:slug>/comment/<uuid:id>/', comment.CommentDetailAPIView.as_view(), name='detail_comment'),
  path('tag/', tag.TagListAPIView.as_view(), name='list_tag'),
  path('tag/create/', tag.TagCreateAPIView.as_view(), name='create_tag'),
  path('tag/<uuid:id>/', tag.TagDetailAPIView.as_view(), name='detail_tag'),
]
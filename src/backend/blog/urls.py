from unicodedata import category
from django.urls import path
from blog.views import tag, post, comment, category

app_name = 'blog'

urlpatterns = [
  path('', post.PostListAPIView.as_view(), name='list_post'),
  path('create/', post.PostCreateAPIView.as_view(), name='create_post'),
  path('tag/', tag.TagListAPIView.as_view(), name='list_tag'),
  path('tag/create/', tag.TagCreateAPIView.as_view(), name='create_tag'),
  path('tag/<str:slug>/', tag.TagDetailAPIView.as_view(), name='detail_tag'),
  path('category/', category.CategoryListAPIView.as_view(), name='list_tag'),
  path('category/create/', category.CategoryCreateAPIView.as_view(), name='create_tag'),
  path('category/<str:slug>/', category.CategoryDetailAPIView.as_view(), name='detail_tag'),
  path('<str:slug>/', post.PostDetailAPIView.as_view(), name='detail_post'),
  path('<str:slug>/comment/', comment.CommentListAPIView.as_view(), name='list_comment'),
  path('<str:slug>/comment/create/', comment.CommentCreateUpdateAPIView.as_view(), name='create_comment'),
  path('<str:slug>/comment/<uuid:id>/', comment.CommentDetailAPIView.as_view(), name='detail_comment'),
]
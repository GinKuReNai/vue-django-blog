from . import settings
from django.contrib import admin
from django.urls import path, re_path, include
from django.contrib.staticfiles.urls import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),                                       # 管理サイト
    path('api/auth/', include('djoser.urls')),                             # ユーザー情報の取得など
    path('api/auth/', include('djoser.urls.jwt')),                         # JWT認証(ログイン認証)
    path('api/posts/', include('blog.urls', namespace='posts_api')),       # API(Posts)
    path('api/profile/', include('user.urls', namespace='profile_api')),   # API(UserProfile)
]

# Media URL
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
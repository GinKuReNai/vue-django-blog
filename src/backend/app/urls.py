from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),                # 管理サイト
    path('api/auth/', include('djoser.urls')),      # ユーザー情報の取得など
    path('api/auth/', include('djoser.urls.jwt')),  # JWT認証(ログイン認証)
    path('api/posts/', include('blog.urls')),       # API(Posts)
    path('api/profile/', include('user.urls')),     # API(UserProfile)
    re_path('', RedirectView.as_view(url='/')),     # トップページにリダイレクト
]

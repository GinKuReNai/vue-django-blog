"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import djoser
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),                # 管理サイト
    path('api/auth/', include('djoser.urls')),      # ユーザー情報の取得
    path('api/auth/', include('djoser.urls.jwt')),  # JWT認証(ログイン認証)
    path('api/', include('api.urls.blog')),              # API
    re_path('', RedirectView.as_view(url='/')),     # トップページにリダイレクト
]

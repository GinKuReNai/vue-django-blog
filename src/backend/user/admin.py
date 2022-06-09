from django.contrib import admin
from django.utils.safestring import mark_safe
from user.models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    """記事投稿・編集用画面"""
    # 表示項目
    list_display = ['user', 'thumbnail', 'background']
    
    fieldsets = [
        ('画像', {'fields' : ['thumbnail', 'background']}),
        ('プロフィール', {'fields' : ['bio']}),
        ('各種URL設定', {'fields' : ['website', 'twitter', 'github']}),
    ]

    def showImage(self, obj):
        if obj.image:
            return mark_safe('<img src="{}" style="width:100px; height:auto;">'.format(obj.image.url))
        return


# Profileの登録
admin.site.register(Profile, ProfileAdmin)
from django.contrib import admin
from django.utils.safestring import mark_safe
from user.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    """記事投稿・編集用画面"""
    # 表示項目
    list_display = ['user', 'showThumbnail', 'showBackground']
    
    fieldsets = [
        ('アカウント', {'fields' : ['user', 'display_name']}),
        ('画像', {'fields' : ['thumbnail', 'background']}),
        ('プロフィール', {'fields' : ['bio']}),
        ('各種URL設定', {'fields' : ['website', 'twitter', 'github', 'linkedin']}),
    ]

    def showThumbnail(self, obj):
        if obj.thumbnail:
            return mark_safe('<img src="{}" style="width:auto; height:200px;">'.format(obj.thumbnail.url))
        return

    def showBackground(self, obj):
        if obj.background:
            return mark_safe('<img src="{}" style="width:auto; height:200px;">'.format(obj.background.url))
        return

# Profileの登録
admin.site.register(Profile, ProfileAdmin)
from rest_framework import serializers

from blog.models import Post

class PostCreateUpdateSerializer(serializers.ModelSerializer):
    """作成・更新時シリアライザ"""
    # authorの出力をusernameに変更
    author = serializers.ReadOnlyField(source='author.username') 
    # ManyToOne関係のComment
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        # 利用するモデルのフィールド
        fields = [
            'title',
            'subtitle',
            'body',
            'meta_description',
            'image',
        ]
    
    def validate_title(self, value):
        """タイトルの文字数を確認"""
        if(len(value)) > 255:
            return serializers.ValidationError('タイトルは255文字以内です。')
        return value

    def validate_subtitle(self, value):
        """サブタイトルの文字数を確認"""
        if(len(value)) > 255:
            return serializers.ValidationError('サブタイトルは255文字以内です。')
        return value
    
    def validate_meta_description(self, value):
        """メタ情報の文字数を確認"""
        if(len(value)) > 150:
            return serializers.ValidationError('メタ情報は150文字以内です。')
        return value
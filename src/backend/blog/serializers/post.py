from rest_framework import serializers

from blog.models import Post, Comment

class PostCreateUpdateSerializer(serializers.ModelSerializer):
    """作成・更新時シリアライザ"""
    class Meta:
        model = Post
        # 利用するモデルのフィールド
        fields = [
            'title',
            'subtitle',
            'body',
            'meta_description',
            'image',
            'tags',
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

class PostListSerializer(serializers.ModelSerializer):
    """リスト時シリアライザ"""
    url = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Post
        fields = [
            'title',
            'subtitle',
            'image',
            'author',
            'meta_description',
            'tags',
            'comments',
            'url',
        ]
    
    def get_comments(self, obj):
        """コメント数を出力"""
        qs = Comment.objects.filter(post=obj).count()
        return qs

    def get_url(self, obj):
        """URLを出力"""
        return obj.get_api_url()

    
class PostDetailSerializer(serializers.ModelSerializer):
    """詳細取得時シリアライザ"""
    slug = serializers.SerializerMethodField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    comments = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Post
        fields = [
            'title',
            'subtitle',
            'slug',
            'body',
            'meta_description',
            'image',
            'date_created',
            'date_modified',
            'publish_date',
            'published',
            'author',
            'tags',
            'comments',
        ]
        
    def get_slug(self, obj):
        """slugを出力"""
        return obj.slug

    def get_comments(self, obj):
        """コメントを出力"""
        qs = Comment.objects.filter(post=obj)
        try:
            serializer = CommentSerializer(qs, many=True)
        except Exception as e:
            print(e)
        return serializer.data


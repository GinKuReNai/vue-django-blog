from rest_framework import serializers

from blog.models import Tag, Post, Comment, Category
from blog.serializers.tag import TagPrimaryKeyRelatedSerializer
from blog.serializers.comment import CommentSerializer


class PostCreateUpdateSerializer(serializers.ModelSerializer):
    """作成・更新時シリアライザ"""
    tags = TagPrimaryKeyRelatedSerializer(many=True, queryset=Tag.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Post
        # 利用するモデルのフィールド
        fields = [
            'id',
            'title',
            'subtitle',
            'body',
            'author',
            'meta_description',
            'image',
            'tags',
            'category',
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
            'id',
            'title',
            'subtitle',
            'image',
            'author',
            'meta_description',
            'tags',
            'comments',
            'url',
            'category',
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
            'id',
            'title',
            'subtitle',
            'slug',
            'body',
            'meta_description',
            'image',
            'created_at',
            'updated_at',
            'author',
            'tags',
            'comments',
            'category',
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
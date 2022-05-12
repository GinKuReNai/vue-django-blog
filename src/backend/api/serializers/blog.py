from rest_framework import serializers

from blog.models import Tag, Post, Comment

class TagSerializer(serializers.ModelSerializer):
    """Tag用シリアライザ"""
    class Meta:
        model = Tag
        # 利用するモデルのフィールド
        fields = ['name']

class PostSerializer(serializers.ModelSerializer):
    """Post用シリアライザ"""
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
            'slug',
            'body',
            'meta_description',
            'author',
            'tags',
            'comments', 
        ]

class CommentSerializer(serializers.ModelField):
    """Comment用シリアライザ"""
    # ManyToOne関係のComment(Reply)
    replies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Comment
        # 利用するモデルのフィールド
        fields = ['name', 'text', 'post', 'parent', 'replies']
        


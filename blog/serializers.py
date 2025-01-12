from rest_framework import serializers
from .models import (
    Post,
    Comment,
    PostView,
    Like,
)
import datetime


class CommentSerializer(serializers.ModelSerializer):
    
    post = serializers.StringRelatedField()
    post_id = serializers.IntegerField(read_only=True)
    commentor = serializers.StringRelatedField()
    commentor_id = serializers.IntegerField(read_only=True)
    created_date = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = (
            "id",
            "post",
            "post_id",
            "title",
            "comment", 
            "commentor", 
            "commentor_id", 
            "created_date")

    def get_created_date(self, obj):
        return datetime.datetime.strftime(obj.created_date, '%d.%m.%Y')


class LikeSerializer(serializers.ModelSerializer):
    
    post = serializers.StringRelatedField()
    post_id = serializers.IntegerField(read_only=True)
    liker = serializers.StringRelatedField()
    liker_id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Like
        fields = (
            "id",
            "post",
            "post_id",
            "liker",
            "liker_id",
            "is_liked",
            )
    
    
class PostSerializer(serializers.ModelSerializer):
    
    author = serializers.StringRelatedField()
    author_id = serializers.IntegerField(read_only=True)
    created_date = serializers.SerializerMethodField()
    
    comments = CommentSerializer(many=True, read_only=True)
    visit_count = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    
        
    class Meta:
        model = Post
        fields = (
            'id',
            'image',
            'title',
            'content',
            'is_published',
            'created_date',
            'author',
            'author_id',
            'comments',
            'slug',
            'visit_count',
            'like_count',
        )
    
    def get_created_date(self, obj):
        return datetime.datetime.strftime(obj.created_date, '%d.%m.%Y')
    
    def get_visit_count(self, obj):
        return PostView.objects.filter(post=obj).count()
    
    def get_like_count(self, obj):
        return Like.objects.filter(post_id=obj.id, is_liked=True).count()
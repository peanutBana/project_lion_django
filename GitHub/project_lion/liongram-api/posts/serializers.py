from calendar import c
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import Comment, Post

class PostBaseModelSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PostListModelSerializer(PostBaseModelSerializer):
    class Meta(PostBaseModelSerializer.Meta):
        fields = [
            'id',
            'image',
            'created_at',
            'view_count',
            'writer',
        ]
        depth = 1
        # exclude = ['content']

class PostRetrieveModelSerializer(PostBaseModelSerializer):
    class Meta(PostBaseModelSerializer.Meta):
        depth = 1


class PostCreateModelSerializer(PostBaseModelSerializer):
    class Meta(PostBaseModelSerializer.Meta):
        fields = [
            'image',
            'content',
        ]


class PostDeleteModelSerializer(PostBaseModelSerializer):
    pass

class CommentListModelSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
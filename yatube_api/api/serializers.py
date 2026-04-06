from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Comment, Post

class FollowSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    following = serializers.StringRelatedField()
    
    class Meta:
        model = Follow
        fields = ('user', 'following')
    
    def validate_following(self, value):
        request = self.context.get('request')
        if request.user == value:
            raise serializers.ValidationError('Нельзя подписаться на самого себя')
        return value
    
    def create(self, validated_data):
        validated_data['user'] = self.context.get('request').user
        return super().create(validated_data)
        
class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment

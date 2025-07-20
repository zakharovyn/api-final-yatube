from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Comment, Post, Group, Follow

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()  # Разрешаем передавать данные
    )

    class Meta:
        model = Follow
        exclude = ('id',)

    def validate_following(self, following):
        """Валидация подписок."""
        user = self.context['request'].user
        if following == user:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя!'
            )
        if Follow.objects.filter(user=user, following=following).exists():
            raise serializers.ValidationError(
                'Вы уже подписаны на этого пользователя!'
            )
        return following

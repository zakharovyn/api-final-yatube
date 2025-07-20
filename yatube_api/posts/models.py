from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class TextField(models.Model):
    text = models.TextField('Текст')

    class Meta:
        abstract = True


class Group(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=200
    )
    slug = models.SlugField(
        'Слаг',
        max_length=50
    )
    description = models.TextField('Описание')


class Post(TextField):
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    image = models.ImageField(
        'Изображение',
        upload_to='posts/',
        null=True,
        blank=True
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='posts',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.text


class Comment(TextField):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="followings",
        null=True,
        blank=True
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='followers',
        null=True,
        blank=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_follow'
            )
        ]

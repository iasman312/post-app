from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(BaseModel):
    title = models.CharField(max_length=300)
    link = models.URLField()
    upvote_amount = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='user_posts',
        null=True,
        blank=True,
    )

    class Meta:
        db_table = 'posts'
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def __str__(self):
        return f'{self.title}'


class Comment(BaseModel):
    content = models.TextField(max_length=3000)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='user_comments',
        null=True,
        blank=True,
    )
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name='comments'
    )

    class Meta:
        db_table = 'comments'
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def __str__(self):
        return f'{self.content}'

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
    upvote_amount = models.PositiveIntegerField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='user_posts'
    )

    class Meta:
        db_table = 'posts'
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def __str__(self):
        return f'{self.title}'




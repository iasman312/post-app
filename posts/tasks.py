from celery import shared_task

from posts.models import Post


@shared_task(name="periodic_deletion")
def periodic_deletion():
    Post.objects.all().update(upvote_amount=0)

from django.dispatch import receiver
from users.models import User
from .models import Problem
from users.models import User
from django.db.models.signals import post_save, post_delete
from django.template.defaultfilters import slugify




# @receiver(post_save, sender=Problem)
def problem_updated(sender,instance, created,  **kwargs):
    if created:
        user = instance
        title = 'your first question'
        problem = Problem.objects.create(
            title = title,
            slug = slugify(title),
            author = user,
            tags = 'first',
            body = None,
        )
@receiver(post_delete, sender=Problem)
def probleme_deleted(sender, instance,**kwargs):
    print('Post deleted')
    print('Post was', instance.title)

post_save.connect(problem_updated,sender=User)
# post_delete.connect(probleme_deleted,sender=Problem)
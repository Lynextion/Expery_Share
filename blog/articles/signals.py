from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from account.models import Profile
from .models import Article

@receiver(post_save, sender=User, update = Article)
def create_last_update(sender, instance, created, **kwargs):
    if created:
        Profile.objects.update(last_update=instance.date)
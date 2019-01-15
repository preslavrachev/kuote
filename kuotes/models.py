from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from djongo import models


class TwitterAccount(models.Model):
    avatar_url = models.URLField(verbose_name='Avatar URL', blank=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    twitter_account = models.EmbeddedModelField(model_container=TwitterAccount)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()


class Source(models.Model):
    url = models.URLField(verbose_name='Source URL')
    image_url = models.URLField(verbose_name='Image URL')


class Kuote(models.Model):
    content = models.CharField(max_length=280)
    slug = models.TextField()
    source = models.EmbeddedModelField(model_container=Source)

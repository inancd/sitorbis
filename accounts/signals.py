from django.db.models.signals import post_save
from django.dispatch import receiver

from django.conf import settings
from accounts.models import Profile, MediaModel


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(author=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_media(sender, instance, created, **kwargs):
    if created:
        MediaModel.objects.create(author=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_media(sender, instance, **kwargs):
    instance.mediamodel.save()



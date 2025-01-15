from django.db.models.signals import post_save
from django.dispatch import receiver
from user.models import CustomUser
from profiles.models import Profile, SocialMedia , WorkHistory , UserSkill , Review


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        WorkHistory.objects.create(user=instance)
        UserSkill.objects.create(user=instance)
        Review.objects.create(user=instance)
        SocialMedia.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

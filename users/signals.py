from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def build_profile(sender, instance, created, **kwargs):
    if created:
        print("build_profile(created): ", ', '.join(['{}={!r}'.format(k, v) for k, v in kwargs.items()]))
        Profile.objects.create(user=instance)
    else:
        print("build_profile(updated): ", ', '.join(['{}={!r}'.format(k, v) for k, v in kwargs.items()]))

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    print("save_profile: ", ', '.join(['{}={!r}'.format(k, v) for k, v in kwargs.items()]))
    instance.profile.save()
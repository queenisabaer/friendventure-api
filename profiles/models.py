from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Profile(models.Model):
    """
    Profile model with one-to-one relationship to User,
    Created automatically on user creation.
    used Code Institute's Django REST Framework walkthrough project
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    profile_image = models.ImageField(
        upload_to='images/', default='../ghost_profile_baukik'
    )
    description = models.TextField(blank=True)
    phone_number = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
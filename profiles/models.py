from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile model with one-to-one relationship to User,
    Created automatically on user creation.
    used Code Institute's Django REST Framework walkthrough project

    Attributes:
    owner (User): A one-to-one reference to the User model, indicating the
     owner of the profile.
    name (str): An optional name of the profile owner.
    profile_image (ImageField): An optional profile image, with a default
     placeholder image.
    description (str): An optional description for the profile.
    phone_number (int): An optional phone number for the profile owner.
    email (str): An optional email address for the profile owner.
    created_at (DateTimeField): A timestamp indicating when the profile was
     created. Automatically set to the current date and time when the profile
     is created.
    updated_at (DateTimeField): A timestamp indicating when the profile was
     last updated. Automatically set to the current date and time whenever the
     profile is updated.

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

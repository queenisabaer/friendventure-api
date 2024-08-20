from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Participant
from friendventures.models import Friendventure


# Used an article by kt775629 (GeeksForGeeks) to achieve this
@receiver(post_save, sender=Friendventure)
def create_owner_participant(sender, instance=None, created=False, **kwargs):
    if created:
        Participant.objects.create(
            owner=instance.owner,
            friendventure=instance
        )

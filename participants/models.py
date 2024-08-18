from django.db import models
from django.contrib.auth.models import User
from friendventures.models import Friendventure


class Participant(models.Model):
    """
    A model representing a participant in a specific friendventure event.

    Attributes:
    owner (User): A foreign key reference to the User model, indicating the user who is participating in the friendventure.
    friendventure (Friendventure): A foreign key reference to the Friendventure model, indicating the friendventure event in which the user is participating.
    created_at (DateTimeField): A timestamp indicating when the participation was created. Automatically set to the current date and time when the participation is created.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    friendventure = models.ForeignKey(
        Friendventure, related_name='participants', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'friendventure']

    def __str__(self):
        return f'{self.owner} {self.friendventure}'
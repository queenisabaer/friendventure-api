from django.db import models
from django.contrib.auth.models import User
from friendventures.models import Friendventure


class Participant(models.Model):
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
from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    A model representing the following relationship between users.

    Attributes:
    owner (User): A foreign key reference to the User model, indicating the
     user who is following another user.
    followed (User): A foreign key reference to the User model, indicating the
     user being followed.
    created_at (DateTimeField): A timestamp indicating when the follow
     relationship was created. Automatically set to the current date and time
     when the relationship is created.
    """
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following'
    )
    followed = models.ForeignKey(
        User, related_name='followed_by', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f'{self.owner} {self.followed}'

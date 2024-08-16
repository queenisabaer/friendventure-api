from django.db import models
from django.contrib.auth.models import User
from friendventures.models import Friendventure


class Comment(models.Model):
    """
    A model representing a comment made by a user on a specific friendventure.

    Attributes:
    owner (User): A foreign key reference to the User model, indicating the user who made the comment.
    friendventure (Friendventure): A foreign key reference to the Friendventure model, indicating the friendventure to which the comment belongs.
    created_at (DateTimeField): A timestamp indicating when the comment was created. Automatically set to the current date and time when the comment is created.
    updated_at (DateTimeField): A timestamp indicating when the comment was last updated. Automatically set to the current date and time whenever the comment is updated.
    content (TextField): The text content of the comment.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    friendventure = models.ForeignKey(Friendventure, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
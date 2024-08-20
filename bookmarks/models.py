from django.db import models
from django.contrib.auth.models import User
from friendventures.models import Friendventure


class Bookmark(models.Model):
    """
    Model representing a bookmark made by a user for a specific friendventure.

    Attributes:
    owner (User): Foreign key reference to the User model, indicating the user
     who created the bookmark.
    friendventure (Friendventure): Foreign key reference to the FriendVenture-
     model, indicating the friendventure that has been bookmarked.
    created_at (DateTimeField): A timestamp indicating when the bookmark was
     created. Automatically set to the current date and time when the bookmark
     is created.
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    friendventure = models.ForeignKey(
        Friendventure, related_name="bookmarks", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["owner", "friendventure"]

    def __str__(self):
        return f"{self.owner} {self.friendventure}"

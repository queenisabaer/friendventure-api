from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

FRIENDVENTURE_CATEGORIES = (
    ('Indoor', 'Indoor'),
    ('Outdoor', 'Outdoor')
)


class Friendventure(models.Model):
    """
    A model representing a friendventure event created by a user.

    Attributes:
    owner (User): A foreign key reference to the User model, indicating the
     user who created the friendventure.
    title (str): The title of the friendventure.
    image (ImageField): An optional image associated with the friendventure,
     with a default placeholder image.
    date (DateField): Date on which the friendventure is scheduled to occur.
    time (TimeField): Time at which the friendventure is scheduled to start.
    place (str): The location where the friendventure will take place.
    description (str): An optional description of the friendventure.
    category (str): The category of the friendventure, chosen from predefined
     options ('Indoor' or 'Outdoor').
    created_at (DateTimeField): A timestamp indicating when the friendventure
     was created. Automatically set to the current date and time when the
     friendventure is created.
    updated_at (DateTimeField): A timestamp indicating when the friendventure
     was last updated. Automatically set to the current date and time whenever
     the friendventure is updated.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to='images/',
        default="../Friendventure_default_swdkd8",
        blank=True
    )
    date = models.DateField()
    time = models.TimeField()
    place = models.TextField()
    description = models.TextField(blank=True)
    category = models.CharField(
        max_length=50,
        choices=FRIENDVENTURE_CATEGORIES,
        default='Outdoor'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_datetime(self):
        """Combine date and time to return a datetime object."""
        return datetime.combine(self.date, self.time)

    class Meta:
        ordering = ['-created_at', 'category', 'date']

    def __str__(self):
        return f'{self.id} {self.title} by {self.owner}'

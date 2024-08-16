from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

FRIENDVENTURE_CATEGORIES = (
    ('Indoor', 'Indoor'),
    ('Outdoor', 'Outdoor')
)


class Friendventure(models.Model):
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

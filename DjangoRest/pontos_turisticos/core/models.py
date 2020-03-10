from django.db import models
from attractions.models import Attraction
from perks.models import Perk
from reviews.models import Review
from comments.models import Comment
from locations.models import Location


class TouristSpot(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    validated = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Attraction)
    perks = models.ManyToManyField(Perk, blank=True)
    reviews = models.ManyToManyField(Review, blank=True)
    comments = models.ManyToManyField(Comment, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

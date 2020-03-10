from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    comment = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    validated = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


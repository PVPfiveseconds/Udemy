from django.db import models


class Perk(models.Model):
    name = models.CharField(max_length=150)
    amount = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

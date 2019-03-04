from django.db import models
from django.contrib.auth.models import User

# Create Food Fitness Application....
class FoodFitnessModel(models.Model):
    userName = models.CharField(max_length=200, default="")
    # password = models.CharField(max_length=200, default="")
    calories = models.IntegerField(default=0)
    date = models.DateField(default = "")

    def __str__(self):
        return self.userName
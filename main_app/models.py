from django.db import models

# Create your models here.
class HealthyFoods(models.Model):
    foodName = models.CharField(max_length=250)
    Ingredients = models.CharField(max_length=555)
    calories = models.IntegerField()
    Protien = models.IntegerField()
    Fiber = models.IntegerField()

    def __str__(self):
        return f'{self.foodName} - {self.calories}'



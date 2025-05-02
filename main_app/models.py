from django.db import models
#from django.contrib.auth.models import User
# Create your models here.
class Collection(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class HealthyFoods(models.Model):
    foodName = models.CharField(max_length=250)
    calories = models.IntegerField()
    Protien = models.IntegerField()
    Fiber = models.IntegerField()
    Ingredients = models.TextField(max_length=555)
    image_url = models.CharField(max_length=255,null=True, blank=True)
    collection = models.ManyToManyField(Collection)

    def __str__(self):
        return f'{self.foodName} - {self.calories} Cals'



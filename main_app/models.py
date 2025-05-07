from django.db import models
from django.contrib.auth.models import User
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
    collection = models.ManyToManyField(Collection,null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return f'{self.foodName} - {self.calories} Cals'
    
class healthyDrinks(models.Model):
    image_url = models.CharField(max_length=255,null=True, blank=True)
    drinkname= models.CharField(max_length=250)
    calories = models.IntegerField()
    Protien = models.IntegerField()    
    Ingredients = models.TextField(max_length=555)
   
    
   
    def __str__(self):
        return f'{self.drinkname} - {self.calories} Cals'

from django.contrib import admin
from .models import HealthyFoods,Collection,healthyDrinks
# Register your models here.
admin.site.register(HealthyFoods)
admin.site.register(Collection)
admin.site.register(healthyDrinks)

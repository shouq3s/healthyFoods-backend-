from rest_framework import serializers
from .models import HealthyFoods, Collection,healthyDrinks
# i used the code from https://www.django-rest-framework.org/api-guide/relations/#nested-relationships
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'

class HealthyFoodsSerializers(serializers.ModelSerializer):
    collection = CollectionSerializer(many=True, read_only=True)
    
    class Meta:
        model = HealthyFoods
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}    

class HealthyDrinksSerializers(serializers.ModelSerializer):
    class Meta:
        model = healthyDrinks
        fields = '__all__'        
      

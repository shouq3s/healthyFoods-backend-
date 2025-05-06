from rest_framework import serializers
from .models import HealthyFoods, Collection,healthyDrinks
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    # Add a password field, make it write-only
    # prevents allowing 'read' capabilities (returning the password via api response)
    password = serializers.CharField(write_only=True)  

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']  
        )
      
        return user
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
      

from rest_framework import serializers
from .models import HealthyFoods

class HealthyFoodsSerializers(serializers.ModelSerializer):
    class Meta:
        model = HealthyFoods
        fields = '__all__'

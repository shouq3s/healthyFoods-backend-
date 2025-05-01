from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import HealthyFoods
from .serializers import HealthyFoodsSerializers
# Create your views here.
class FoodsListCreateView(APIView):
    def get(self,request):
        Foods = HealthyFoods.objects.all()
        serializer = HealthyFoodsSerializers(Foods, many=True)
        return Response(serializer.data,status=200) 
    def post(self,request):
        serializer = HealthyFoodsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class FoodsDetailsView(APIView):
    def get_object(self,pk):
        #saves us from calling get_object_or_404 in every method  
        return get_object_or_404(HealthyFoods,pk=pk)
    
    def get(self,request,pk):
        foods =self.get_object(pk)
        serializer=HealthyFoodsSerializers(foods)
        return Response(serializer.data , status = 200)
    def delete(self,request,pk):
        foods =self.get_object(pk)
        foods.delete()
        return Response(status=204)
    def patch(self,request,pk):
        foods = self.get_object(pk)
        serializer=HealthyFoodsSerializers(foods,data=request.data)#JSON data that will comeing with the request
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)#return the updated it to the api
        return Response(serializer.errors, status=400)
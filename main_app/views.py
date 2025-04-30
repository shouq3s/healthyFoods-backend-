from rest_framework.views import APIView
from rest_framework.response import Response
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

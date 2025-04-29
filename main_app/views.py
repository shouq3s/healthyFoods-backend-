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
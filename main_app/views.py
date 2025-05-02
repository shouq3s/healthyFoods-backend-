from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.password_validation import validate_password
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404
from .models import HealthyFoods
from .serializers import HealthyFoodsSerializers

# Create your views here.
class FoodsListCreateView(APIView):
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
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
    
class SignUpView(APIView):
    permission_classes = [AllowAny]
    # When we recieve a POST request with username, email, and password. Create a new user.
    def post(self, request):
      
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            validate_password(password)
        except ValidationError as err:
            return Response({'error': err.messages}, status=400)

        # Actually create the user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # create an access and refresh token for the user and send this in a response
        tokens = RefreshToken.for_user(user)
        return Response(
            {
                'refresh': str(tokens),
                'access': str(tokens.access_token)
            },
            status=201
        )
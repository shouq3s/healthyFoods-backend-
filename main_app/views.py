from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.password_validation import validate_password
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework import generics, status, permissions
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from .models import HealthyFoods,Collection,healthyDrinks
from .serializers import HealthyFoodsSerializers,CollectionSerializer,HealthyDrinksSerializers,UserSerializer
from rest_framework.generics import ListAPIView

# Create your views here.
# i took this code from https://medium.com/@sydney.idundun/understanding-views-in-django-rest-framework-d78ca8042f04
class CollectionList(ListAPIView):
    permission_classes = [AllowAny]  
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
@api_view(['POST'])
@permission_classes([AllowAny])
def add_collection_to_foods(request, foods_id, collection_id):
    try:
        foods = HealthyFoods.objects.get(pk=foods_id)
        collection = Collection.objects.get(pk=collection_id)
        foods.collection.add(collection)
        return Response({'message': 'Collection was Added!'}, status=200)
    except HealthyFoods.DoesNotExist:
        return Response({'error': 'The foods Does Not Exist'}, status=404)
    except Collection.DoesNotExist:
        return Response({'error': 'The Collection Does Not Exist'}, status=404)
    except:
        return Response({'error': 'Something went wrong'}, status=500)
@api_view(['POST'])
@permission_classes([AllowAny])
def remove_collection_from_foods(request, foods_id, collection_id):
    try:
    
        foods = HealthyFoods.objects.get(pk=foods_id)
        collection = Collection.objects.get(pk=collection_id)
        if foods.collection.filter(id=collection.id).exists():
            foods.collection.remove(collection)
            return Response({'message': 'collection was Removed!'}, status=200)
        else:
            return Response({'message': 'The collection is in the DB but it is not on the foods!'})
    except HealthyFoods.DoesNotExist:
        return Response({'error': 'The foods Does Not Exist'}, status=404)
    except Collection.DoesNotExist:
        return Response({'error': 'The collection Does Not Exist'}, status=404)
    except:
        return Response({'error': 'Something went wrong'}, status=500)

class FoodsListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        #user=request.user
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
class DrinksListCreateView(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        drinks = healthyDrinks.objects.all()
        serializer = HealthyDrinksSerializers(drinks, many=True)
        return Response(serializer.data,status=200)    
    def post(self,request):
        serializer = HealthyDrinksSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400) 
    
class DrinksDetailsView(APIView):
    permission_classes = [AllowAny]
    def get_object(self,pk):
        return get_object_or_404(healthyDrinks,pk=pk)
    
    def get(self,request,pk):
        drinks =self.get_object(pk)
        serializer=HealthyDrinksSerializers(drinks)
        return Response(serializer.data , status = 200)
    def delete(self,request,pk):
        drinks =self.get_object(pk)
        drinks.delete()
        return Response(status=204)
    def patch(self, request, pk):
        drinks = self.get_object(pk)
        serializer = HealthyDrinksSerializers(drinks, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
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

class LoginView(APIView):
  permission_classes = [AllowAny]
  def post(self, request):
    try:
      username = request.data.get('username')
      password = request.data.get('password')
      user = authenticate(username=username, password=password)
      if user:
        refresh = RefreshToken.for_user(user)
        content = {'refresh': str(refresh), 'access': str(refresh.access_token),'user': UserSerializer(user).data}
        return Response(content, status=status.HTTP_200_OK)
      return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as err:
      return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

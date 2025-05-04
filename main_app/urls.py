from django.urls import path
from .views import FoodsListCreateView , FoodsDetailsView,SignUpView,add_collection_to_foods,CollectionList,DrinksListCreateView,DrinksDetailsView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('healthyfoods/', FoodsListCreateView.as_view() , name ='create-foods-list'),
    path('healthydrinks/', DrinksListCreateView.as_view() , name ='create-drinks-list'),
    path('healthyfoods/<int:pk>/',FoodsDetailsView.as_view(),name='foods_detail' ),  
    path('healthydrinks/<int:pk>/',DrinksDetailsView.as_view(),name='drinks_detail' ),  
    path('collections/', CollectionList.as_view(), name='collection'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('healthyfoods/<int:foods_id>/add-collection/<int:collection_id>/', add_collection_to_foods, name='add-collection-to-foods'),


]
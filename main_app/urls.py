from django.urls import path
from .views import FoodsListCreateView , FoodsDetailsView

urlpatterns = [
    path('healthyfoods/', FoodsListCreateView.as_view() , name ='create-foods-list'),
    path('healthyfoods/<int:pk>/',FoodsDetailsView.as_view(),name='foods_detail' )

]
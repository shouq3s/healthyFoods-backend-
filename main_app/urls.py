from django.urls import path
from .views import FoodsListCreateView

urlpatterns = [
    path('healthyfoods/', FoodsListCreateView.as_view() , name ='create-foods-list')
]
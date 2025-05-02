from django.urls import path
from .views import FoodsListCreateView , FoodsDetailsView,SignUpView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('healthyfoods/', FoodsListCreateView.as_view() , name ='create-foods-list'),
    path('healthyfoods/<int:pk>/',FoodsDetailsView.as_view(),name='foods_detail' ),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', SignUpView.as_view(), name='signup')

]
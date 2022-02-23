from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path
from . import views


urlpatterns = [
    path('login/', obtain_jwt_token),
    path('signup/', views.signup),
    path('<str:username>/', views.profile),
    path('<str:username>/update/', views.update)
    
    
]

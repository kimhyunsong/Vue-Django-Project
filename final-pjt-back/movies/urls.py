from django.urls import path
from . import views

urlpatterns = [
   path('', views.movie),
   path('<int:movie_pk>/', views.movie_detail),
   path('<int:movie_pk>/review/', views.movie_review),
   path('<int:movie_pk>/review/<int:review_pk>', views.review_detail),
   path('<int:movie_pk>/likes/', views.movie_likes),
   path('<int:movie_pk>/watched/', views.movie_watched),
   path('search/<str:movieName>/', views.movie_search),
   path('recommend/<str:username>/', views.movie_recommend_logined),
    
]


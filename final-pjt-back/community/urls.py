from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.community, name='index'),
    path('<int:page>/', views.community_detail),
    path('<int:page>/comment/', views.comment_list),
    path('<int:page>/comment/<int:comment_pk>', views.comment_list_detail),
    path('<int:page>/likes/', views.post_likes),
]

from django.urls import path, include 
from plants import views 

urlpatterns = [
    path('home/', views.index, name='index'),
]
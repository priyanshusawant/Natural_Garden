from django.urls import path, include 
from plants import views 

app_name = 'plants'

urlpatterns = [
    path('home/', views.index, name='index'),
    path('detail/<int:item_id>', views.detail, name='detail'),
]
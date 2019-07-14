from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('delete/<int:pk>/', views.delete_address, name='delete_address')
]
    # path('get_gps/<int:pk>/', views.get_gps, name='get_gps'),
    # path('get_all_gps/', views.get_all_gps, name='get_all_gps')

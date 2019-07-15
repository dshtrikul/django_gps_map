from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('delete/<int:pk>/', views.delete_address, name='delete_address'),
    path('render_map/', views.render_map, name='render_map')

]

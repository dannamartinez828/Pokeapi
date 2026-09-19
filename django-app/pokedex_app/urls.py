from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('consultar/', views.consultar, name='consultar'),
    path('consultar-local/', views.consultar_local, name='consultar_local'),
]

from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('error/', views.error, name='error'),
    path('board/', views.board, name='board'),
    path('obtener_localidades/', views.obtener_localidades, name='obtener_localidades'),
    path('localidades/', views.lista_localidades, name='lista_localidades'),
    path('search/', views.search, name='search'),

]

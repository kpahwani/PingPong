from django.urls import path
from . import views

app_name = "players"
urlpatterns = [
    path('', views.index, name='index'),
    path('create_player/', views.create_player, name='create_player'),
    path('join_game/', views.join_game, name='join_game'),
]

from django.urls import path
from . import views

app_name = "referee"
urlpatterns = [
    path('', views.index, name='index'),
    path('all_players/', views.list_active_players, name='list_players'),
    path('start_game/', views.start_game, name='start_game'),
    path('activate_users/', views.set_all_user_active, name='activate_users'),
    path('get_results/', views.get_results, name='get_results')
]
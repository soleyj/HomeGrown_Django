# accounts/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path(r'',views.DashboardView.as_view(), name='home'),
    path('props',views.PropsView.as_view(), name='props'),
    path('pistas',views.AutoPistasView.as_view(), name='pistas'),
    path('game_config',views.GameConfigView.as_view(), name='game_config'),
]
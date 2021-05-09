from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inibalance', views.inibalance),
    path('addExpence', views.addExpence),
    path('display', views.display),
]

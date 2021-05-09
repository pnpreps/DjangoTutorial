from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.home, name="home"),
 	path('addperson', views.addperson,),
 	path('display', views.display),
 	path('delete', views.delete),
 	path('update', views.update),
]
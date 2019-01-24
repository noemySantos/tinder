from django.urls import path
from . import views

urlpatterns = [
    path ('', views.home),
    path ('usuario/', views.usuario_list),
    path ('usuario/<int:usuario_id>/', views.usuario_show),

]                                             
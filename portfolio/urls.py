from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('imsp/', views.imsp, name='imsp'),
    path('mtg/', views.mtg, name='mtg'),
    path('snhu/', views.snhu, name='snhu'),
]
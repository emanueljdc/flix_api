
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('actors/', views.ActorListCreateAPIView.as_view(), name='actor_create_list'),
    path('actors/<int:pk>', views.ActorRetrieveUpdateDestroyAPIView.as_view(), name='actor_detail'),

]

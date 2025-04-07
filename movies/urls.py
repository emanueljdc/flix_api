
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('movies/', views.MovieListCreateAPIView.as_view(), name='movie_create_list'),
    path('movies/<int:pk>', views.MovieRetrieveUpdateDestroyAPIView.as_view(), name='movie_detail'),

]

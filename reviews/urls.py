
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('reviews/', views.ReviewListCreateAPIView.as_view(), name='review_create_list'),
    path('reviews/<int:pk>', views.ReviewRetrieveUpdateDestroyAPIView.as_view(), name='review_detail'),

]

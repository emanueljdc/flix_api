
from django.urls import path
# from genres.views import GenreListCreateAPIView, GenreRetrieveUpdateDestroyAPIView
from . import views

urlpatterns = [

    path('genres/', views.GenreListCreateAPIView.as_view(), name='genre_create_list'),
    path('genres/<int:pk>', views.GenreRetrieveUpdateDestroyAPIView.as_view(), name='genre_detail'),

    # path('genres/', GenreListCreateAPIView.as_view(), name='genre_create_list'),
    # path('genres/<int:pk>', GenreRetrieveUpdateDestroyAPIView.as_view(), name='genre_detail'),

]

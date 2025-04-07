# import json
# from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import render, get_object_or_404
# from django.http import JsonResponse
# from rest_framework import 

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from genres.models import Genre
from genres.serializers import GenreSerializer


class GenreListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer



# @csrf_exempt
# def genre_create_list_view(request):
#     if request.method == 'GET':
#         geners = Genre.objects.all()
#         # data=[]
#         # for gener in geners:
#         #     data.append(
#         #         {'id': gener.id, 'name': gener.name}
#         #     )
           
#         data = [{'id': gener.id, 'name': gener.name} for gener in geners]
#         return JsonResponse(data, safe=False)
    
#     elif request.method == 'POST':
#         data = json.loads(request.body.decode('utf-8'))

#         new_genre = Genre(name=data['name']) 
#         new_genre.save()
#         return JsonResponse(
#             {'id': new_genre.id, 'name':new_genre.name},
#             status=201,
#             )


# @csrf_exempt
# def genre_detail_view(request, pk):
#     # genre = Genre.objects.get(pk=pk)
#     # data = {'id': genre.id, 'name': genre.name}
#     # return JsonResponse(data, safe=False)
#     genre = get_object_or_404(Genre, pk=pk)

#     if request.method == 'GET':
#         # genre = Genre.objects.get(pk=pk)
#         genre = get_object_or_404(Genre, pk=pk)
         
#         data = {'id': genre.id, 'name': genre.name}
#         return JsonResponse(data, safe=False)
    
#     elif request.method == 'PUT':
#         data = json.loads(request.body.decode('utf-8'))
#         genre.name = data['name']
#         genre.save()
#         return JsonResponse(
#             {'id': genre.id, 'name':genre.name},
#             status=201,
#             )
    
#     elif request.method == 'DELETE':
#         genre.delete()
#         return JsonResponse(
#             {'message': 'Genero excluido com sucesso.'},
#             status=204,
#             )


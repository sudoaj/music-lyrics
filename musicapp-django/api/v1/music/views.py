from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Artiste, Album, Song
from .serializers import ArtisteSerializer, SongSerializer

class SongView(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class ArtisteView(viewsets.ModelViewSet):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer




# class MusicViews(APIView):
#     def get(self, request):
#         musics = Music.objects.all()
#         return Response({"articles": musics})

#     def post(self, request):
#         music = request.data.get()
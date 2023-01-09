from rest_framework import serializers
from .models import Artiste, Album, Song

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = ('id', 'name', 'title', 'other_title_1', 'other_title_multiple', 'artiste_art', 'album_art_thumbnail', 'firstName', 'lastName', 'created_at', 'updated_at')


# class ArtisteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Artiste
#         fields = ('id', 'name', 'title', 'other_title_1', 'other_title_multiple', 'artiste_art', 'album_art_thumbnail', 'firstName', 'lastName', 'created_at', 'updated_at')


       

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'song_name', 'artiste', 'artiste_fetures', 'is_explicit', 'music_genre', 'lyrics', 'description', 'song_file', 'song_snippet', 'song_file_link', 'song_music_video','song_music_video_link','song_art', 'song_album_art','created_at', 'updated_at', 'person1', 'additional_information')


    
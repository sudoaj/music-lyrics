from django.contrib import admin
from .models import Album, Song, Artiste

class ArtisteAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',"updated_at")
    list_display = ["name", "firstName", "lastName"]

class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',"updated_at")
    list_display = ["album_name", "artiste", "description"]
    
    
class SongAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',"updated_at")
    list_display = ( "song_name", "artiste", "description")

admin.site.register(Artiste, ArtisteAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)



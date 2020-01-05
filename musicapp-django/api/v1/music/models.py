from django.db import models
from django.utils import timezone
from django_auto_one_to_one import AutoOneToOneModel


song_genre= (
    
       (1, 'hipop'),
        (2, 'afro'),
        (3, 'indie'),
        (4, 'k-pop'),
        (5, 'pop'),
)



song_contribution = (
      (1, 'Singer'),
        (2, 'Rapper'),
        (3, 'Vocals'),
         (4, 'Piano'),
         (5, 'Beats Maker'),    
)
# Aritst Table
class Artiste(models.Model):
    name = models.CharField("Artiste Name", max_length=51)
    title = models.IntegerField(choices=song_contribution, default ="1")
    other_title_1 = models.CharField("What did you Contribute? Piano, Composer? Beats? Smoke?", max_length=25, blank=True)
    other_title_multiple = models.CharField("Enter Tittle comma seperetad", max_length=1000, blank=True)
   
    artiste_art = models.ImageField(upload_to = 'artiste_art_images/', default = 'images/no-img.jpg', blank=True) 
    album_art_thumbnail = models.ImageField(upload_to = 'album_art_thumbnails/', default = 'images/no-img.jpg', blank=True) 


    firstName = models.CharField("First Name", max_length=25)
    lastName = models.CharField("Last Name", max_length=25)
    created_at = models.DateTimeField("Date Created", auto_now_add=True) 
    updated_at = models.DateTimeField("Date Updated", auto_now=True)
    
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Artiste, self).save(*args, **kwargs)

# Album Table
class Album(models.Model):
    album_name = models.CharField("Album Name", max_length=51)
    artiste = models.ForeignKey('Artiste', on_delete=models.CASCADE, related_name="album")
    songs = models.ManyToManyField('Song', related_name="songs")
    album_art = models.ImageField(upload_to = 'album_art_images/', default = 'images/no-img.jpg', blank=True) 

    description = models.TextField()
    created_at = models.DateTimeField("Date Created", auto_now_add=True)
    updated_at = models.DateTimeField("Date Updated", auto_now=True)

    def get_songs(self):
        return "\n".join([p.song for p in self.songs.all()])
    
        
    def __str__(self):
        return self.album_name
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        # print (created_at)    
        return super(Album, self).save(*args, **kwargs)


# Song Table
class Song(models.Model):
    # song creators
    song_name = models.CharField("Song Name", max_length=51)
    artiste = models.ForeignKey('Artiste', on_delete=models.CASCADE, related_name="song")
    artiste_fetures = models.ManyToManyField('Artiste', related_name="song_features", blank=True)
    
    # song metadata
    is_explicit = models.BooleanField("Check if the song contain explicit content", default=True)
    music_genre = models.IntegerField(choices=song_genre, default ="1")
    lyrics = models.TextField()
    description = models.TextField()
    
    # song media
    song_file = models.FileField(upload_to='song_audio/', default= 'audio/def.mp3', blank=True)
    song_snippet = models.FileField(upload_to='song_audio_snippet/', default= 'audio/def.mp3' , blank=True)
    song_file_link = models.URLField(max_length = 200, blank=True) 
    song_music_video = models.FileField(upload_to='song_music_video/', default= 'audio/def.mp3', blank=True)
    song_music_video_link = models.URLField(max_length = 200, blank=True) 
    song_art = models.ImageField(upload_to = 'song_art_images/', default = 'images/no-img.jpg', blank=True) 
    song_album_art = models.ImageField(upload_to = 'song_art_images/', default = 'images/no-img.jpg', blank=True)    

    
    # song time/duration
    created_at = models.DateTimeField("Date Created", auto_now_add=True)
    updated_at = models.DateTimeField("Date Updated", auto_now=True)

    # Additonal Creators
    person1 = models.ManyToManyField('Artiste', related_name="song_creator_1", blank=True)
    

    
    # additional information
    additional_information = models.TextField(default="None")



    #get the url of the object
    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"id": self.id})
    # return song name
    def __str__(self):
        return self.song_name
    # on save, do this
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Song, self).save(*args, **kwargs)
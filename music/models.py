from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Album(models.Model):
    artist = models.CharField(max_length=250)   #varialbe artist will be a column in database
    album_title = models.CharField(max_length=500) #CharField indicates what type of data is stored
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def get_absolute_url(self):     #after filling in the form with above details where they need to be redircted is written here
        return reverse('music:detail', kwargs={'pk':self.pk}) #kwargs means key word args
    '''Whenever we take details view it take primary key of the album thats why
    we are using kwargs in order to pass pk to the details view'''

    def __str__(self): #String representaion of Album object in database shell in order to print the values of Album object
        return self.album_title + '-' + self.artist #Whenever you type Album.objects.all() you will get values in this format instead of Object Return

class Song(models.Model):       #Song needs to be part of album and we need to link it by ForeignKey
    album = models.ForeignKey(Album, on_delete=models.CASCADE)  #on_delete means when we delete Album any songs linked to album will also be deleted
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    #Creating a String representation of Song
    def __str__(self):
        return self.song_title
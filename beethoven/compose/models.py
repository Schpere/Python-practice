from django.db import models

# Create your models here.

class Song(models.Model):
    song_title = models.CharField(max_length=200)
    pub_date = models.DateTimefield('date created')
    song_structure = models.TextField('sheet music')
    file_path = models.FilePathField(path='/home/harald/.beep/songs')
    def __str__(self):
        return self.song_title

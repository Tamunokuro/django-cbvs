from enum import Flag
import re
from django.db import models
from django.urls import reverse

# Create your models here.
class Album(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)
    created = models.TimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core:album_detail', kwargs={'pk':self.pk})

      

class Artist(models.Model):
    name = models.CharField(null=False, blank=False, max_length=64)
    track = models.CharField(null=True, blank=True, max_length=255)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True, max_length=255, related_name='collection_artist')
    created = models.TimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('core:artist_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    def count(self):
        b = Artist.objects.all()
        for artist in b:
            c = artist.collection_artist.all().count()
        return reverse('core:artist_detail', f'{artist.name}  has {c} album(s)')

    class Meta:
        ordering = ('name',)




class Collection(models.Model):
    slug = models.SlugField(max_length=255)
    track = models.CharField(null=True, blank=True, max_length=255)
    artist = models.ForeignKey(Artist, null=True, blank=True, on_delete=models.CASCADE, related_name='collection_artist')
    album = models.ForeignKey(Album, null=True, blank=True, on_delete=models.CASCADE, related_name='collection_album')
    created = models.TimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)


    def __str__(self):
        return self.track

    
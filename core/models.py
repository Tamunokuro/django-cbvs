from django.db import models
from django.urls import reverse

# Create your models here.
class Artist(models.Model):
    name = models.CharField(null=False, blank=False, max_length=64)
    created = models.TimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('core:artist_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created',)


class Collection(models.Model):
    title = models.CharField(null=False, blank=False, max_length=255)
    artist = models.ForeignKey(Artist, null=False, blank=False, on_delete=models.CASCADE, related_name='collection_artist')



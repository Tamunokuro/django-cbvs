from django.forms.models import inlineformset_factory
from .models import Artist, Collection, Album

ArtistCollection = inlineformset_factory(Artist, Collection, fields=('track', 'album'), extra=5)
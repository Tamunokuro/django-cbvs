from django.forms.models import inlineformset_factory
from .models import Artist, Collection

ArtistCollection = inlineformset_factory(Artist, Collection, fields=('title',))
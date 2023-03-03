from django.contrib import admin
from .models import Artist, Collection, Album
# Register your models here.


class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name','album']

class CollectionAdmin(admin.ModelAdmin):
    list_display= ['artist', 'album', 'track', 'slug']
    prepopulated_fields = {'slug': ('track',), }

class AlbumAdmin(admin.ModelAdmin):
    list_display= ['name', 'created',]


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Album, AlbumAdmin)

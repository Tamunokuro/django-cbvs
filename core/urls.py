from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.ArtistView.as_view(), name='home'),
    path('create/', views.ArtistCreateView.as_view(), name='create_artist'),
    path('artists/',views.ArtistListView.as_view(), name='artist_list'),
    path('artist/<int:pk>/',views.ArtistDetailView.as_view(), name='artist_detail'),
    path('add-edit/<int:pk>/album/edit/', views.ArtistEditView.as_view(), name='album-edit'),
    path('album/',views.AlbumCreateView.as_view(), name='create_album'),
    path('album-list/',views.AlbumListView.as_view(), name='album_list'),
    path('album-detail/<int:pk>', views.AlbumDetailView.as_view(), name='album_detail')
    


]

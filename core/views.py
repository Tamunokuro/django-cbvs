import imp
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, FormView
from django.contrib import messages

from .models import Artist
from .forms import ArtistCollection


# Create your views here.
class ArtistView(TemplateView):
    template_name = 'home.html'

class ArtistListView(ListView):
    model = Artist
    template_name = 'artist_list.html'

class ArtistDetailView(DetailView):
    model = Artist
    template_name = 'artist_detail.html'

class ArtistCreateView(CreateView):
    model = Artist
    template_name = 'artist_create.html'
    fields = ['name',]

    def form_valid(self, form):

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Artist Created Successfully'
        )
        return super().form_valid(form)
    


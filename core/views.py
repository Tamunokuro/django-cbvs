import imp
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, FormView
from django.contrib import messages
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponseRedirect
from django.urls import reverse

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

class ArtistEditView(SingleObjectMixin, FormView):
    model = Artist
    template_name = 'artist_collection.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset= Artist.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset= Artist.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return ArtistCollection(**self.get_form_kwargs(), instance=self.object)

    def get_success_url(self):
        return reverse('core:artist_detail', kwargs={'pk':self.object.pk})
    
    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Successfull'
        )
        return HttpResponseRedirect(self.get_success_url())


from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView

from .models import Singer, Song
from .forms import SingerForm, SongForm


class SongListView(ListView):
    model = Song
    fields = ["title", "album", "singer"]
    template_name = 'song/song_list.html'
    context_object_name = 'songs'


class SongDetailView(DetailView):
    model = Song
    fields = ["title", "album", "singer"]
    template_name = 'song/song_detail.html'


class SongCreateView(CreateView):
    model = Song
    fields = ["title", "album", "singer"]
    template_name = 'song/add_song.html'
    context_object_name = 'songs'
    success_url = reverse_lazy('song-list')


class SongDeleteView(DeleteView):
    model = Song
    fields = ["title", "album", "singer"]
    template_name = 'song/song_confirm_delete.html'
    success_url = reverse_lazy('song-list')


class SongUpdateView(UpdateView):
    model = Song
    form_class = SongForm
    template_name = 'song/song_edit.html'
    success_url = reverse_lazy('song-list')


class SingerListView(ListView):
    model = Singer
    fields = ["name", "lastname"]
    template_name = 'singer/singer_list.html'
    context_object_name = 'singers'


class SingerDetailView(DetailView):
    model = Singer
    fields = ["name", "lastname"]
    template_name = 'singer/singer_detail.html'


class SingerCreateView(CreateView):
    model = Singer
    fields = ["name", "lastname"]
    template_name = 'singer/add_singer.html'
    context_object_name = 'singer'
    success_url = reverse_lazy('singer-list')


class SingerDeleteView(DeleteView):
    model = Singer
    fields = ["name", "lastname"]
    template_name = 'singer/singer_confirm_delete.html'
    success_url = reverse_lazy('singer-list')


class SingerUpdateView(UpdateView):
    model = Singer
    form_class = SingerForm
    template_name = 'singer/add_singer.html'
    success_url = reverse_lazy('singer-list')




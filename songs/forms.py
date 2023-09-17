from django import forms
from .models import Singer, Song


class SingerForm(forms.ModelForm):
    class Meta:
        model = Singer
        fields = ["name", "lastname"]


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ["title", "album", "singer"]

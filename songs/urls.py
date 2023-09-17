from django.urls import path
from .views import (SongCreateView, SongDeleteView, SongListView, SongUpdateView, SongDetailView, SingerDeleteView,
                    SingerDetailView, SingerUpdateView, SingerListView, SingerCreateView)

urlpatterns = [
    path('', SongListView.as_view(), name="song-list"),
    path('add/', SongCreateView.as_view(), name="add-song"),
    path('delete/<int:pk>', SongDeleteView.as_view(), name="delete-song"),
    path('update/<int:pk>', SongUpdateView.as_view(), name="song-update"),
    path('<int:pk>/', SongDetailView.as_view(), name="detail-song"),

    path('singers/add/', SingerCreateView.as_view(), name="add-singer"),
    path('singers/delete/<int:pk>', SingerDeleteView.as_view(), name="delete-singer"),
    path('singers/', SingerListView.as_view(), name="singer-list"),
    path('singers/update/<int:pk>', SingerUpdateView.as_view(), name="singer-update"),
    path('singers/<int:pk>/', SingerDetailView.as_view(), name="detail-singer"),
]

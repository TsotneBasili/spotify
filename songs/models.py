from django.db import models


class Singer(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)


class Song(models.Model):
    title = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)





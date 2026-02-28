from django.db import models
from django.urls import reverse


class Artist(models.Model):
    name = models.CharField('name', max_length=200, unique=True)
    banner =models.ImageField(default="fallback.png", blank=True)
    my_order = models.PositiveIntegerField(default=0,blank=False,null=False)

    class Meta:
        ordering = ['my_order']
        
    def __str__(self):
        return self.name




class Track(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    played_on = models.DateField(blank=False)
    played_at = models.TimeField(blank=False)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("playlist:track_detail", args=[str(self.id)])


from django.db import models
from django.db.models import Q, CheckConstraint, UniqueConstraint
from django.urls import reverse


ARTICLES = [
    ('The', 'The'),
    ('A', 'A')
]


class Artist(models.Model):
    name = models.CharField('Name', max_length=200, unique=True)
    aka = models.CharField('Aka', max_length=200, blank=True)
    article = models.CharField('Article', max_length=10, choices=ARTICLES, blank=True)
    banner =models.ImageField(default="fallback.jpg", blank=True)



    @property
    def display_name(self):
        if self.article == '':
            val = self.name
        else:
            val = ''.join([self.article,' ', self.name])
        return val


    class Meta:
        ordering = ['name']
        constraints = [
            CheckConstraint(
                condition= Q(aka="") 
                | ~Q(aka__icontains=" ") & ~Q(aka__icontains="_"),
                violation_error_message="Aka may be blank a string that excludes underscores and spaces",
                name="%(app_label)s_%(class)s_aka_rule"
            ),
         
        ]
     
        

    def __str__(self):
        return self.display_name




class Track(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    played_on = models.DateField(blank=False)
    played_at = models.TimeField(blank=False)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("playlist:track_detail", args=[str(self.id)])
    




class NewTrack(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='track_artist')
    collaborators = models.ManyToManyField(Artist, related_name='track_collaborator')

    class Meta:
        ordering = ['title']
        constraints = [
            UniqueConstraint(fields=["title", "artist"], name="unique_track"),
        ]


    def __str__(self):
        return self.title


    

class Entry(models.Model):
    track = models.ForeignKey(NewTrack, on_delete=models.CASCADE)
    played_on = models.DateField(blank=False)
    played_at = models.TimeField(blank=False)


    class Meta:
        ordering = ['-played_on', '-played_at', 'track__title']
        constraints = [
            UniqueConstraint(fields=["played_on", "played_at"], name="unique_entry"),
        ]


    def __str__(self):
        return self.track.title

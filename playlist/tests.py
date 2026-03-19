from django.test import TestCase
from django.db.models import Subquery, Count, OuterRef, Max
from playlist.models import Track


# Create your tests here.
summary = Track.objects.filter(
    artist__name=OuterRef('artist__name'), 
    title=OuterRef('title')
).values(
    'title',
    'artist__name'
).annotate(
    total=Count('artist__name')
)

main = Track.objects.values(
    'title',
    'artist__id', 
    'artist__name',
    'artist__article',
    'artist__banner'

).annotate(
    total=Subquery(summary.values('total')[:1])
).filter(total__gte=3).order_by('-total')

for item in main:
    print(item)

#############################

summary = Track.objects.filter(
    artist__name=OuterRef('artist__name'), 
    title=OuterRef('title')
).values(
    'title', 
    'artist__name'
).annotate(
    total=Count('artist__name')
)

main = Track.objects.annotate(
    total=Subquery(summary.values('total')[:1])
).filter(total__gte=3).order_by('-total')

for item in main:
    print(item)





track_total = len(Track.objects.filter(
    artist__name='Madonna', 
    title='Express Yourself'
))


m =Track.objects.filter(
    artist__name='Madonna', 
    title='Express Yourself'
).annotate(
    total=Max(track_total)
)
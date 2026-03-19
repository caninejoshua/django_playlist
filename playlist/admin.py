from django.contrib import admin
from .models import Track, Artist, NewTrack, Entry




class TrackAdmin(admin.ModelAdmin):
    list_display=('played_on', 'played_at', 'title', 'artist')


class ArtistAdmin(admin.ModelAdmin):
    list_display=('name', 'banner', 'article', 'aka')



class EntryAdmin(admin.ModelAdmin):
    list_display=('played_on', 'played_at', 'track')


class NewTrackAdmin(admin.ModelAdmin):
    list_display=('title', 'artist', 'other_artists')

    def other_artists(self, obj):
        return obj.collaborators.count()





admin.site.register(Track, TrackAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(NewTrack, NewTrackAdmin)
admin.site.register(Entry, EntryAdmin)
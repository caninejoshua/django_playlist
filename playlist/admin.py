from django.contrib import admin
from .models import Track, Artist
from adminsortable2.admin import SortableAdminMixin

admin.site.register(Track)

@admin.register(Artist)
class ArtistAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'my_order')


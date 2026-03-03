from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Track
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator


def is_valid_queryparam(param):
    return param != '' and param is not None


def home(request):
    qs = Track.objects.all().order_by("played_on", "-played_at")

    

    title_or_artist_query = request.GET.get('title_or_artist')
    date_min = request.GET.get("date_min")
    date_max = request.GET.get("date_max")
   
    if is_valid_queryparam(title_or_artist_query):
        qs = qs.filter(Q(title__icontains=title_or_artist_query)
                       | Q(artist__name__icontains=title_or_artist_query)
                       ).distinct()
        tlabel = title_or_artist_query
    else:
        tlabel = ""

    if is_valid_queryparam(date_min):
        qs =  qs.filter(played_on__gte=date_min)
        slabel = date_min
    else:
        slabel=""
    
    if is_valid_queryparam(date_max):
        qs =  qs.filter(played_on__lte=date_max)
        elabel = date_max
    else:
        elabel= ""

# Pagination
    p = Paginator(qs,12)
    page = request.GET.get("page")
    qs = p.get_page(page)            

    context = {
         "queryset": qs,
         "slabel": slabel,
         "elabel": elabel,
         "tlabel": tlabel
         }

    return render(request, 'playlist/home.html', context)


# View Details
def track_details(request, pk):
    track = get_object_or_404(Track, pk=pk)
    return render(request, 'playlist/track_detail.html', {"track": track})







from django.views.generic import ListView
from .models import Listing


class ListingListView(ListView):
    model = Listing
    template_name = 'listings/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(city='santiago')

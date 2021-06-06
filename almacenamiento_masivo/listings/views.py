from django.views.generic import ListView
from listings.models import Listing


class ListingListView(ListView):
    model = Listing
    template_name = 'listings/list.html'

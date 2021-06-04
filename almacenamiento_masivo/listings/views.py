from django.views.generic import ListView
from listings.models import Listing
from base.api import run_api


class ListingListView(ListView):
    model = Listing
    template_name = 'listings/list.html'

    run_api()

from django.urls import path
from . import views

urlpatterns = [
    path(
        'list/',
        views.ListingListView.as_view(),
        name='listings_list',
    )
]

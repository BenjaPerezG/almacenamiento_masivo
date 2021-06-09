from django.urls import path
from . import views


urlpatterns = [
    path(
        'listings_per_city/',
        views.ListingsPerCityView.as_view(),
        name='listings_per_city'
    ),
    path(
        'availability_per_month/',
        views.AvailabilityPerMonth.as_view(),
        name='availability_per_month'
    ),
    path(
        'room_type_per_city/',
        views.RoomTypePerCity.as_view(),
        name='room_type_per_city'
    ),
    path(
        'minimum_nights_per_city/',
        views.MinimumNightsPerCity.as_view(),
        name='minimum_nights_per_city'
    )
]

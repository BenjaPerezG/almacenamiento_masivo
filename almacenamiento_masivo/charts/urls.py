from django.urls import path
from . import views


urlpatterns = [
    path(
        'listings_per_city/',
        views.ListingsPerCityView.as_view(),
        name='listings_per_city'
    )
]

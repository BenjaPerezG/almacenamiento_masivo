from django.shortcuts import render
from django.views.generic import TemplateView


class ListingsPerCityView(TemplateView):
    template_name = 'charts/listings_per_city.html'

class AvailabilityPerMonth(TemplateView):
    template_name = 'charts/availability_per_month.html'

class RoomTypePerCity(TemplateView):
    template_name = 'charts/room_type_per_city.html'

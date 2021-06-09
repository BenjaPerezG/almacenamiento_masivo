from django.shortcuts import render
from django.views.generic import TemplateView
import json


class ListingsPerCityView(TemplateView):
    template_name = 'charts/listings_per_city.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # llamada a api con query y devuelta de json
        json_dict = {
            'santiago': 25,
            'buenos aires': 30,
            'bogota': 46
        }
        context['json'] = json.dumps(json_dict, indent=4)
        return context


class AvailabilityPerMonth(TemplateView):
    template_name = 'charts/availability_per_month.html'


class RoomTypePerCity(TemplateView):
    template_name = 'charts/room_type_per_city.html'

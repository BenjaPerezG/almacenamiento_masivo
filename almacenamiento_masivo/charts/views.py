from django.shortcuts import render
from django.views.generic import TemplateView
import json
from base.api import run_api
from base.utils import countries, cities


class ListingsPerCityView(TemplateView):
    template_name = 'charts/listings_per_city.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        result = run_api('SELECT * from grupo3_db.totallistingsbycity')
        data = json.loads(result)
        for dict in data:
            dict['county'] = countries[dict['city']]
            dict['city'] = cities[dict['city']]
            dict['data'] = dict.pop('totalAlojamientos')

        print(data)

        # llamada a api con query y devuelta de json
        context['json'] = json.dumps(data, indent=4)
        return context


class AvailabilityPerMonth(TemplateView):
    template_name = 'charts/availability_per_month.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        result = run_api('SELECT date, disponibles, -(ocupados) as ocupados FROM availability_per_month')
        data = json.loads(result)
        for dict in data:
            print(dict)

        # llamada a api con query y devuelta de json
        context['json'] = json.dumps(data, indent=4)
        return context


class RoomTypePerCity(TemplateView):
    template_name = 'charts/room_type_per_city.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        result = run_api('SELECT * from grupo3_db.type_room_per_city')
        data = json.loads(result)
        for dict in data:
            dict['city'] = cities[dict['city']]

        # llamada a api con query y devuelta de json
        context['json'] = json.dumps(data, indent=4)
        return context

class MinimumNightsPerCity(TemplateView):
    template_name = 'charts/minimum_nights_per_city.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        result = run_api('select * from grupo3_db.average_min_nights order by minimum_nights_average desc')
        data = json.loads(result)
        for dict in data:
            dict['county'] = countries[dict['city']]
            dict['city'] = cities[dict['city']]
            dict['data'] = dict.pop('minimum_nights_average')

        print(data)

        # llamada a api con query y devuelta de json
        context['json'] = json.dumps(data, indent=4)
        return context

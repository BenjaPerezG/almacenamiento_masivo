from django.shortcuts import render
from django.views.generic import TemplateView


class ListingsPerCityView(TemplateView):
    template_name = 'charts/listings_per_city.html'

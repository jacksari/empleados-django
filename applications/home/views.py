from django.shortcuts import render
from django.views.generic import TemplateView, ListView


class PruebaView(TemplateView):
    template_name = 'home/prueba.html'


class PruebaListView(ListView):
    queryset = ['1', '2', '3', '4', '5', '6']
    context_object_name = 'numeros'
    template_name = 'home/lista.html'

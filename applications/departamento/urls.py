from django.contrib import admin
from django.urls import path


def desde(self):
    print('======================DESDE DEPARTAMENTO==================')


urlpatterns = [
    path('departamento/', desde),
]

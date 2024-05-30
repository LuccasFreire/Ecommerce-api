

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.get_produtos, name="produtos"),
]

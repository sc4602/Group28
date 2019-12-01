from django.urls import path
from django.contrib import admin
from . import views

urlpatterns =[
        path('sightings/<int:squirrel_id>/',views.detaol_sighting),
        path('map/', views.display_map),
        path('sightings/', views.list_sightings),
        path('sightings/add', views.add_sighting),
        path('sightings/stats', views.stats_sightings)
        ]

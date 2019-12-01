from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('map/', views.display_map),
    path('sightings/', views.list_sightings),
    path('sightings/<unique_squirrel_id>', views.detail_sighting),
    path('sightings/add', views.add_sighting),
    path('sightings/stats', views.stats_sightings),
]


from django.shortcuts import render

from django.http import HttpResponse

# GET
def display_map(request):
    return HttpResponse('A view that shows a map '
                        'that displays the location of the squirrel sightings '
                        'on an OpenStreets map.')


# GET
def list_sightings(request):
    return HttpResponse('A view to list all squirrel sightings with links to edit and add sightings.')


# POST or DELETE
def detail_sighting(request, unique_squirrel_id):
    return HttpResponse('A view to update or delete: %s' % unique_squirrel_id)


# POST
def add_sighting(request):
    return HttpResponse('A view to create a new sighting.')


# GET
def stats_sightings(request):
    return HttpResponse('A view with general stats about the sightings')

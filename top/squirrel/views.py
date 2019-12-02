from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from . import models


# GET
def display_map(request):
    return HttpResponse('A view that shows a map '
                        'that displays the location of the squirrel sightings '
                        'on an OpenStreets map.')


# GET
def list_sightings(request):
    if request.method == 'GET':
        squirrel_list = models.Sighting.objects.all()
        return render(request, 'squirrel/list_sighting.html',locals())


    return HttpResponse('A view to list all squirrel sightings with links to edit and add sightings.')


# POST or DELETE
def detail_sighting(request, unique_squirrel_id):
    return HttpResponse('A view to update or delete: %s' % unique_squirrel_id)


# POST
@csrf_exempt
def add_sighting(request):
    if request.method == 'POST':
        # return HttpResponse("POST Response")
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        unique_squirrel_id = request.POST.get('unique_squirrel_id')
        shift = request.POST.get('shift')
        date = request.POST.get('date')
        age = request.POST.get('age')
        primary_fur_color = request.POST.get('primary_fur_color')
        location = request.POST.get('location')
        specific_location = request.POST.get('specific_location')
        running = request.POST.get('running')
        chasing = request.POST.get('chasing')
        climbing = request.POST.get('climbing')
        eating = request.POST.get('eating')
        foraging = request.POST.get('foraging')
        other_activities = request.POST.get('other_activities')
        kuks = request.POST.get('kuks')
        quaas = request.POST.get('quaas')
        moans = request.POST.get('moans')
        tail_flags = request.POST.get('tail_flags')
        tail_twitches = request.POST.get('tail_twitches')
        approaches = request.POST.get('approaches')
        indifferent = request.POST.get('indifferent')
        runs_from = request.POST.get('runs_from')

        new_squirrel = models.Sighting(longitude=longitude,
                                       latitude=latitude,
                                       unique_squirrel_id=unique_squirrel_id,
                                       shift=shift,
                                       date=date,
                                       age=age,
                                       primary_fur_color=primary_fur_color,
                                       location=location,
                                       specific_location=specific_location,
                                       running=running,
                                       chasing=chasing,
                                       climbing=climbing,
                                       eating=eating,
                                       foraging=foraging,
                                       other_activities=other_activities,
                                       kuks=kuks,
                                       quaas=quaas,
                                       moans=moans,
                                       tail_flags=tail_flags,
                                       tail_twitches=tail_twitches,
                                       approaches=approaches,
                                       indifferent=indifferent,
                                       runs_from=runs_from)
        new_squirrel.save()
        return render(request, 'squirrel/add_sighting.html')
    # return HttpResponse('A view to create a new sighting.')


# GET
def stats_sightings(request):
    return HttpResponse('A view with general stats about the sightings')

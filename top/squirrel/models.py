# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Sighting(models.Model):
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    unique_squirrel_id = models.CharField(primary_key=True, max_length=20)
    shift = models.CharField(max_length=3, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    age = models.CharField(max_length=10, blank=True, null=True)
    primary_fur_color = models.CharField(max_length=10, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    specific_location = models.TextField(blank=True, null=True)
    running = models.IntegerField(blank=True, null=True)
    chasing = models.IntegerField(blank=True, null=True)
    climbing = models.IntegerField(blank=True, null=True)
    eating = models.IntegerField(blank=True, null=True)
    foraging = models.IntegerField(blank=True, null=True)
    other_activities = models.TextField(blank=True, null=True)
    kuks = models.IntegerField(blank=True, null=True)
    quaas = models.IntegerField(blank=True, null=True)
    moans = models.IntegerField(blank=True, null=True)
    tail_flags = models.IntegerField(blank=True, null=True)
    tail_twitches = models.IntegerField(blank=True, null=True)
    approaches = models.IntegerField(blank=True, null=True)
    indifferent = models.IntegerField(blank=True, null=True)
    runs_from = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Sighting'

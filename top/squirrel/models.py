# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Sighting(models.Model):
    index = models.BigIntegerField(primary_key=True, blank=True, null=False)
    longitude = models.TextField(blank=True, null=True)  # This field type is a guess.
    latitude = models.TextField(blank=True, null=True)  # This field type is a guess.
    unique_squirrel_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    shift = models.TextField(blank=True, null=True)  # This field type is a guess.
    date = models.TextField(blank=True, null=True)
    age = models.TextField(blank=True, null=True)  # This field type is a guess.
    primary_fur_color = models.TextField(blank=True, null=True)  # This field type is a guess.
    location = models.TextField(blank=True, null=True)  # This field type is a guess.
    specific_location = models.TextField(blank=True, null=True)
    running = models.BooleanField(blank=True, null=True)
    chasing = models.BooleanField(blank=True, null=True)
    climbing = models.BooleanField(blank=True, null=True)
    eating = models.BooleanField(blank=True, null=True)
    foraging = models.BooleanField(blank=True, null=True)
    other_activities = models.TextField(blank=True, null=True)
    kuks = models.BooleanField(blank=True, null=True)
    quaas = models.BooleanField(blank=True, null=True)
    moans = models.BooleanField(blank=True, null=True)
    tail_flags = models.BooleanField(blank=True, null=True)
    tail_twitches = models.BooleanField(blank=True, null=True)
    approaches = models.BooleanField(blank=True, null=True)
    indifferent = models.BooleanField(blank=True, null=True)
    runs_from = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Sighting'

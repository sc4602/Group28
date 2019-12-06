# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


TRUE = 'True'
FALSE = 'False'
Boolean_Choice = (
    (TRUE, 'True'),
    (FALSE, 'False'),
)

AM = 'Am'
PM = 'Pm'
Shift_Choice = (
    (AM, 'AM'),
    (PM, 'PM'),
)

Adult = 'Adult'
Juvenile = 'Juvenile'
Age_Choice = (
    (Adult, "Adult"),
    (Juvenile, "Juvenile"),
)


class Sighting(models.Model):
    index = models.BigIntegerField(primary_key=True, blank=True, null=False)
    longitude = models.FloatField(blank=True, null=True)  # This field type is a guess.
    latitude = models.FloatField(blank=True, null=True)  # This field type is a guess.
    unique_squirrel_id = models.CharField(max_length=14)  # This field type is a guess.
    shift = models.CharField(max_length=2, null=True, choices=Shift_Choice)  # This field type is a guess.
    date = models.DateField(blank=True, null=True)
    age = models.CharField(max_length=10, blank=True, choices=Age_Choice)  # This field type is a guess.
    primary_fur_color = models.TextField(blank=True, null=True)  # This field type is a guess.
    location = models.TextField(blank=True, null=True)  # This field type is a guess.
    specific_location = models.TextField(blank=True, null=True)
    running = models.BooleanField(choices=Boolean_Choice)
    chasing = models.BooleanField(choices=Boolean_Choice)
    climbing = models.BooleanField(choices=Boolean_Choice)
    eating = models.BooleanField(choices=Boolean_Choice)
    foraging = models.BooleanField(choices=Boolean_Choice)
    other_activities = models.TextField(blank=True, null=True)
    kuks = models.BooleanField(choices=Boolean_Choice)
    quaas = models.BooleanField(choices=Boolean_Choice)
    moans = models.BooleanField(choices=Boolean_Choice)
    tail_flags = models.BooleanField(choices=Boolean_Choice)
    tail_twitches = models.BooleanField(choices=Boolean_Choice)
    approaches = models.BooleanField(choices=Boolean_Choice)
    indifferent = models.BooleanField(choices=Boolean_Choice)
    runs_from = models.BooleanField(choices=Boolean_Choice)

    class Meta:
        managed = True
        db_table = 'Sighting'

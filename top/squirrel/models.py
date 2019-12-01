from django.db import models

class Sighting(models.Model):
    SHIFT_CHOICES = (
        ('AM', 'AM'),
        ('PM', 'PM')
    )
    longitude = models.FloatField()
    latitude = models.FloatField()
    unique_squirrel_id = models.CharField(max_length=20, unique=True)
    shift = models.CharField(max_length=2, choices=SHIFT_CHOICES)
    date = models.CharField(max_length=8)  # MM-DD-YYYY
    age = models.CharField(max_length=10, null=True, default='')
    primary_fur_color = models.CharField(max_length=10, null=True, default='')
    location = models.CharField(max_length=30, null=True, default='')
    specific_location = models.CharField(max_length=30, null=True, default='')
    running = models.BooleanField()
    chasing = models.BooleanField()
    climbing = models.BooleanField()
    eating = models.BooleanField()
    foraging = models.BooleanField()
    other_activities = models.TextField()
    kuks = models.BooleanField()
    quaas = models.BooleanField()
    moans = models.BooleanField()
    tail_flags = models.BooleanField()
    tail_twitches = models.BooleanField()
    approaches = models.BooleanField()
    indifferent = models.BooleanField()
    runs_from = models.BooleanField()

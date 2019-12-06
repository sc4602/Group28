from django.core.management.base import BaseCommand

from squirrel.models import Sighting
import csv


class Command(BaseCommand):
    help = 'Export the data in database into csv'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help="Input data path")

    def handle(self, *args, **options):
        headers = ['longitude', 'latitude', 'unique squirrel id', 'shift', 'date', 'age', 'primary fur color',
                   'location', 'specific_location', 'running', 'chasing', 'climbing', 'eating', 'foraging',
                   'other activities', 'kuks', 'quaas', 'moans', 'tail flags', 'tail twitches', 'approaches',
                   'indifferent', 'runs from']
        with open(options['path'], 'w') as fp:
            writer = csv.writer(fp)
            writer.writerow(headers)
            squirrels = Sighting.objects.all()
            for squirrel in squirrels:
                row = []
                for field in Sighting._meta.fields:
                    row.append(getattr(squirrel, field.name))
                writer.writerow(row)

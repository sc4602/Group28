from django.core.management.base import BaseCommand
import pandas as pd
from sqlalchemy import create_engine, String, Float, Boolean, Date, Text

change_column_names = {
    'X': 'longitude',
    'Y': 'latitude',
    'Unique Squirrel ID': 'unique_squirrel_id',
    'Shift': 'shift',
    'Date': 'date',
    'Age': 'age',
    'Primary Fur Color': 'primary_fur_color',
    'Location': 'location',
    'Specific Location': 'specific_location',
    'Running': 'running',
    'Chasing': 'chasing',
    'Climbing': 'climbing',
    'Eating': 'eating',
    'Foraging': 'foraging',
    'Other Activities': 'other_activities',
    'Kuks': 'kuks',
    'Quaas': 'quaas',
    'Moans': 'moans',
    'Tail flags': 'tail_flags',
    'Tail twitches': 'tail_twitches',
    'Approaches': 'approaches',
    'Indifferent': 'indifferent',
    'Runs from': 'runs_from'
}

dtypedict = {
    'longitude': Float,
    'latitude': Float,
    'unique_squirrel_id': String(20),
    'shift': String(3),
    'date': Date,
    'age': String(10),
    'primary_fur_color': String(10),
    'location': String(30),
    'specific_location': Text,
    'running': Boolean,
    'chasing': Boolean,
    'climbing': Boolean,
    'eating': Boolean,
    'foraging': Boolean,
    'other_activities': Text,
    'kuks': Boolean,
    'quaas': Boolean,
    'moans': Boolean,
    'tail_flags': Boolean,
    'tail_twitches': Boolean,
    'approaches': Boolean,
    'indifferent': Boolean,
    'runs_from': Boolean
}


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help="Input data path")

    def handle(self, **kwargs):
        df = pd.read_csv(kwargs['path'])
        df['Date'] = pd.to_datetime(df.Date, format='%m%d%Y')
        conn = create_engine("mysql+pymysql://root:rootroot@localhost/squirrel", encoding='utf-8')
        df.rename(columns=change_column_names, inplace=True)
        df = df[dtypedict.keys()]
        df.to_sql(name='Sighting', con=conn, if_exists='replace', index=False, dtype=dtypedict)

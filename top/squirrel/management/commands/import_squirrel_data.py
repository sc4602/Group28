from django.core.management.base import BaseCommand
import pandas as pd


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help="Input data path")

    def handle(self, **kwargs):
        df = pd.read_csv(kwargs["path"])
        print(df.head())

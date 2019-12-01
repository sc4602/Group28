from django.core.mangement.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help="Input data path")

    def handle(self, **kwargs):
        print(kwargs["path"])

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import csv

def import_squirrel_data(path_to_file):
    with open(path_to_file, 'r', encodeing = 'UTF-8') as raw_data:
        lines = csv.reader(raw_data,delimiter = ',')
    return lines

def export_squirrel_data():
    pass


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quirrel.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    if sys.argv[2] == 'import_squirrel_data':
        import_squirrel_data(sys.argv[3])
    elif sys.argv[2] == 'export_squirrel_data':
        export_squirrel_data(sys.argv[3])
    else:
        print('ERROR')



if __name__ == '__main__':
    main()

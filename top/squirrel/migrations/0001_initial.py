# Generated by Django 2.2.7 on 2019-11-28 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sighting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('unique_squirrel_id', models.CharField(max_length=20, unique=True)),
                ('shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], max_length=2)),
                ('date', models.CharField(max_length=8)),
                ('age', models.CharField(default='', max_length=10, null=True)),
                ('primary_fur_color', models.CharField(default='', max_length=10, null=True)),
                ('location', models.CharField(default='', max_length=30, null=True)),
                ('specific_location', models.CharField(default='', max_length=30, null=True)),
                ('running', models.BooleanField()),
                ('chasing', models.BooleanField()),
                ('climbing', models.BooleanField()),
                ('eating', models.BooleanField()),
                ('foraging', models.BooleanField()),
                ('other_activities', models.TextField()),
                ('kuks', models.BooleanField()),
                ('quaas', models.BooleanField()),
                ('moans', models.BooleanField()),
                ('tail_flags', models.BooleanField()),
                ('tail_twitches', models.BooleanField()),
                ('approaches', models.BooleanField()),
                ('indifferent', models.BooleanField()),
                ('runs_from', models.BooleanField()),
            ],
        ),
    ]

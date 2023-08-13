# Generated by Django 4.2.4 on 2023-08-05 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Geoname',
            fields=[
                ('geonameid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('asciiname', models.CharField(max_length=200)),
                ('alternatenames', models.CharField(blank=True, max_length=10000)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('featureclass', models.CharField(max_length=1)),
                ('featurecode', models.CharField(max_length=10)),
                ('countrycode', models.CharField(max_length=2)),
                ('population', models.IntegerField()),
                ('elevation', models.IntegerField()),
                ('dem', models.IntegerField()),
                ('timezone', models.CharField(max_length=40)),
                ('modification_date', models.DateField()),
            ],
        ),
    ]
import re

from django.core.management.base import BaseCommand
from info_geo.models import Geoname


class Command(BaseCommand):
    help = 'Загружать данные о географических названиях'

    def process_record(self, record):
        fields = re.split(r'\t+', record)
        if len(fields) == 13:
            fields.insert(3, 'пусто')
        if len(fields) == 14:
            geonameid, name, asciiname, alternatenames, latitude, longitude, featureclass, featurecode, countrycode, population, elevation, dem, timezone, modification_date = fields

            try:
                Geoname.objects.create(
                    geonameid=geonameid,
                    name=name,
                    asciiname=asciiname,
                    alternatenames=alternatenames,
                    latitude=float(latitude),
                    longitude=float(longitude),
                    featureclass=featureclass,
                    featurecode=featurecode,
                    countrycode=countrycode,
                    population=int(population),
                    elevation=int(elevation),
                    dem=int(dem),
                    timezone=timezone,
                    modification_date=modification_date
                )
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Ошибка при обработке записи: {record} - {e}"))
        else:
            self.stdout.write(self.style.ERROR(f"Пропуск недопустимой записи: {record}"))

    def handle(self, *args, **options):
        with open('RU.txt', 'r', encoding='utf-8') as data:
            for line in data:
                self.process_record(line.strip())

        self.stdout.write(self.style.SUCCESS('Данные успешно загружены'))

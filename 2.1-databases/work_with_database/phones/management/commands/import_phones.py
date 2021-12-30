import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.template.defaultfilters import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # TODO: Добавьте сохранение модели
            print(phone)
            # p = Phone(id=phone['id'], name=phone['name'], price=phone['price'], image=phone['image'], release_date=phone['release_date'], lte_exists=phone['lte_exists'], slug = slugify(phone['name']))
            # p.save()
            p = Phone.objects.create(id=phone['id'], name=phone['name'], price=phone['price'], image=phone['image'], release_date=phone['release_date'], lte_exists=phone['lte_exists'], slug=slugify(phone['name']))
            pass

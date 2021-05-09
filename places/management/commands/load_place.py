import json.decoder
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.core.files.base import ContentFile

from places.models import Place, Image

import requests


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('place_url', type=str)

    def handle(self, *args, **options):
        place_url = options['place_url']
        try:
            place_response = requests.get(place_url)
            place_response.raise_for_status()
            serialised_place = place_response.json()
        except requests.exceptions.RequestException as error:
            raise CommandError(error)
        except json.decoder.JSONDecodeError:
            raise CommandError(f"Can't get JSON content from {place_url}")
        place, place_created = Place.objects.get_or_create(
            title=serialised_place['title'],
            defaults={
                'description_short': serialised_place['description_short'],
                'description_long': serialised_place['description_long'],
                'latitude': serialised_place['coordinates']['lat'],
                'longitude': serialised_place['coordinates']['lng'],
            }
        )
        for image_url in serialised_place['imgs']:
            image_name = Path(image_url).name
            try:
                image_response = requests.get(image_url)
                image_response.raise_for_status()
            except requests.exceptions.RequestException as error:
                raise CommandError(error)

            image_file = ContentFile(image_response.content)
            append_image_to_place(image_name, image_file, place)


def append_image_to_place(image_name, image_file, place):
    image_entry = Image(place=place)
    image_entry.save()
    image_entry.file.save(image_name, image_file, save=True)
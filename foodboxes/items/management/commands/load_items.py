import os

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from tqdm import tqdm
from urllib3.util import parse_url

from items.models import Item


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-u', '--url', required=True)

    def handle(self, *args, **options):
        url = options['url']

        response = requests.get(url)
        response.raise_for_status()

        items = response.json()

        for item_dict in tqdm(items, desc='items loading'):
            id_ = item_dict['id']
            title = item_dict['title']
            description = item_dict['description']
            weight = item_dict['weight_grams']
            price = item_dict['price']
            img_url = item_dict['image']
            size = item_dict['size']
            cat = item_dict['cat']

            item, _ = Item.objects.update_or_create(id=id_,
                                                    defaults={'title': title,
                                                              'description': description,
                                                              'weight': weight,
                                                              'price': price,
                                                              },
                                                    )
            try:
                img_response = requests.get(img_url)
                img_response.raise_for_status()

                img_filename = get_filename_from_url(img_url)
                item.image.save(img_filename, ContentFile(img_response.content))

            except (requests.exceptions.HTTPError, requests.exceptions.MissingSchema):
                pass


def get_filename_from_url(url):
    parsed_url = parse_url(url)
    _, filename = os.path.split(parsed_url.path)

    return filename

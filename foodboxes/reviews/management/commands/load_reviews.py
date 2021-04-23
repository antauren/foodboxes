import datetime as dt

import requests
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils import timezone
from tqdm import tqdm

from reviews.models import Review

User = get_user_model()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-u', '--url', required=True)

    def handle(self, *args, **options):
        url = options['url']

        response = requests.get(url)
        response.raise_for_status()

        reviews = response.json()

        dt_format = '%Y-%m-%d'

        for review_dict in tqdm(reviews, desc='reviews loading'):
            try:
                id_ = review_dict['id']
                author_id = review_dict['author']
                content = review_dict['content']

                created_at = timezone.make_aware(dt.datetime.strptime(review_dict['created_at'], dt_format))
                published_at = timezone.make_aware(dt.datetime.strptime(review_dict['published_at'], dt_format))

                review_status = review_dict['status']

                if review_status == 'published':
                    status = Review.PUBLISHED
                elif review_status == 'new':
                    status = Review.ON_MODERATION
                else:
                    status = Review.REJECTED

                author = User.objects.filter(id=author_id).first()
                if not author:
                    continue

                review, _ = Review.objects.update_or_create(id=id_,
                                                            defaults={'author': author,
                                                                      'text': content,
                                                                      'created_at': created_at,
                                                                      'published_at': published_at,
                                                                      'status': status,
                                                                      },
                                                            )
            except Exception as err:
                error_text = '{}: {}'.format(err.__class__.__name__, err)
                tqdm.write(error_text)

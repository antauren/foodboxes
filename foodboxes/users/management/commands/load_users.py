import requests
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from tqdm import tqdm

User = get_user_model()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-u', '--url', required=True)

    def handle(self, *args, **options):
        url = options['url']

        response = requests.get(url)
        response.raise_for_status()

        users = response.json()

        for user_dict in tqdm(users, desc='users loading'):

            try:
                email = user_dict['email']
                info = user_dict['info']

                username = email.split('@')[0]

                user, _ = User.objects.update_or_create(
                    id=user_dict['id'],
                    defaults={
                        'password': user_dict['password'],
                        'phone': user_dict['contacts']['phoneNumber'],
                        'middle_name': info['patronymic'],
                        'username': username,
                        'address': user_dict['city_kladr'],
                        'email': email,
                        'first_name': info['name'],
                        'last_name': info['surname'],
                    },
                )
            except Exception as err:
                error_text = '{}: {}'.format(err.__class__.__name__, err)
                tqdm.write(error_text)

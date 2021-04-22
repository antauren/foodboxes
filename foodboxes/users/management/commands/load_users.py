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
                id_ = user_dict['id']

                email = user_dict['email']
                password = user_dict['password']
                info = user_dict['info']
                contacts = user_dict['contacts']
                city_kladr = user_dict['city_kladr']
                premium = user_dict['premium']

                surname = info['surname']
                name = info['name']
                patronymic = info['patronymic']

                phoneNumber = contacts['phoneNumber']
                username = email.split('@')[0]

                user, _ = User.objects.update_or_create(id=id_,
                                                        defaults={'password': password,
                                                                  'phone': phoneNumber,
                                                                  'middle_name': patronymic,
                                                                  'username': username,
                                                                  'address': city_kladr,
                                                                  'email': email,
                                                                  'first_name': name,
                                                                  'last_name': surname,
                                                                  },
                                                        )
            except Exception as err:
                error_text = '{}: {}'.format(err.__class__.__name__, err)
                tqdm.write(error_text)

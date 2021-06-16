from django.core.management.base import BaseCommand
from adminer.models import Competition, Group, Runner, Wrist
from faker import Faker
import random
from random import randrange


class Command(BaseCommand):
    help = 'My awesome generating data tool'    # noqa

    # def handle(self, *args, **options):
    #     fake = Faker()
    #     source_list = [
    #         '',
    #         '',
    #         '',
    #     ]
    #     for i in range(100):
    #         Competition.objects.create(
    #             moneytype='',
    #             sale=round(random.uniform(20.00, 29.99), 2),
    #             buy=round(random.uniform(20.00, 29.99), 2),
    #             source=source_list[randrange(3)],
    #         )
    #     for i in range(100):
    #         Runner.objects.create(
    #              email_from=fake.free_email(),
    #              subject=fake.text(max_nb_chars=50),
    #              message=fake.text(max_nb_chars=200),
    #          )
    #
    #     Wrist.objects.create(
    #         name='',
    #         url='/',
    #     )

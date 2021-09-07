from django.core.management.base import BaseCommand
from adminer.models import Settings, Competition, Group, Runner, Wrist
from faker import Faker
import random
from random import randint
from adminer.tools import *

# queryset_runner = Runner.objects.filter(runner_competition_id=competition_id)
# for i in queryset_runner:
#     i.runner_group_id = randint(41, 80)
#     i.save()


# python manage.py sqlite3 db.sqlite3
# .tables
# DELETE FROM adminer_competition;
# DELETE FROM sqlite_sequence WHERE name = 'adminer_competition';


# make freeze):
#
#
# freeze:
#     pip freeze | grep -v "pkg-resources" > requirements.txt

# Runner.objects.all().delete()
class Command(BaseCommand):
    help = 'My awesome generating data tool'    # noqa

    def handle(self, *args, **options):
        fake = Faker()
        competition_ = Competition.objects.all()[0]
        for j in range(100):
            Wrist.objects.create(
                                competition=competition_,
                                wrist_sn=j,
                                wrist_firmware=57,
                                wrist_voltage=randint(30, 60),
                                wrist_seq=generate_rand_seq(randint(3, 5)),
                                wrist_punches=generate_rand_punch(randint(3, 5)),
                                )

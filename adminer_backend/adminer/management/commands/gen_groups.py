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
    help = 'My awesome generating data tool'  # noqa

    def handle(self, *args, **options):
        competition_ = Competition.objects.all()[0]

        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='M-12', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='M-14', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='M-16', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='M-18', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='M-20', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='M-21', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='M-21A', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='M-21E', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='M-35', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='M-40', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='M-45', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='M-50', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='M-55', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='M-60', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='M-65', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='M-70', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='M-75', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='M-80', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='M-O', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='M-N', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='W-12', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='W-14', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='W-16', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='W-18', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='W-20', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='W-21', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='W-21A', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='W-21E', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='W-35', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='W-40', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='W-45', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='W-50', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='W-55', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='W-60', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='W-65', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='W-70', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='W-75', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='W-80', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='W-O', )
        Group.objects.create(competition=competition_,
                             group_seq=generate_rand_seq(randint(3, 5)),
                             group_name='W-N', )

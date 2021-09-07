from django.core.management.base import BaseCommand
from adminer.models import Settings, Competition, Group, Runner, Wrist
from faker import Faker
from random import randint

class Command(BaseCommand):
    help = 'My awesome generating data tool'    # noqa

    def handle(self, *args, **options):
        fake = Faker()

        groups = Group.objects.all()
        for group in groups:
            for j in range(25):
                Runner.objects.create(
                    runner_sn=j,
                    runner_name=fake.name(),
                    runner_club=fake.word(),
                    runner_coach=fake.first_name(),
                    runner_skill=fake.currency_code(),
                    runner_state=fake.state(),
                    group=group,
                )

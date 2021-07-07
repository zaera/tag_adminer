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
        Settings.objects.create(printer_ip='192.168.11.50',
                                printer_autoprint=True,
                                current_comp_id=1,
                                version=1,)
        for i in range(5):
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='M-12', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='M-14', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='M-16', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='M-18', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='M-20', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='M-21', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='M-21A', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='M-21E', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='M-35', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='M-40', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='M-45', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='M-50', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='M-55', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='M-60', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='M-65', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='M-70', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='M-75', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='M-80', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='M-O', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='M-N', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='W-12', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='W-14', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='W-16', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='W-18', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='W-20', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='W-21', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='W-21A', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='W-21E', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='W-35', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='W-40', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='W-45', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='W-50', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='W-55', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='W-60', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='W-65', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='W-70', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='W-75', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='W-80', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='W-O', )
            Group.objects.create(group_competition_id=i,
                                 group_seq=generate_rand_seq(randint(3, 5)),
                                 group_name='W-N', )
        Competition.objects.create(
                 comp_name='Kupava',
                 comp_type=1,
                 comp_data='text description',
             )
        Competition.objects.create(
                 comp_name='Rogaining 2021',
                 comp_type=1,
                 comp_data='text description',
             )
        Competition.objects.create(
                 comp_name='MTBO Spring',
                 comp_type=1,
                 comp_data='text description',
             )
        Competition.objects.create(
                 comp_name='Sirius 2020',
                 comp_type=1,
                 comp_data='text description',
             )
        Competition.objects.create(
            comp_name='Kocherezhki',
            comp_type=1,
            )
        for i in range(5):
            for j in range(100):
                Runner.objects.create(
                    runner_sn=j,
                    runner_competition_id=i,
                    runner_group_id=randint(0, 20),
                    runner_name=fake.name(),
                    runner_club=fake.word(),
                    runner_coach=fake.first_name(),
                    runner_skill=fake.currency_code(),
                    runner_state=fake.state(),
                )
        for i in range(5):
            for j in range(100):
                Wrist.objects.create(
                                    wrist_competition_id=i,
                                    wrist_sn=j,
                                    wrist_firmware=57,
                                    wrist_voltage=randint(30, 60),
                                    # wrist_passed=bool(random.getrandbits(1)),
                                    # wrist_total_time=9595,
                                    # wrist_points=0,
                                    wrist_seq=generate_rand_seq(randint(3, 5)),
                                    wrist_punches=generate_rand_punch(randint(3, 5)),
                                    )

# queryset_runner = Runner.objects.filter(runner_competition_id=competition_id)
# for i in queryset_runner:
#     i.runner_group_id = randint(41, 80)
#     i.save()
# wrist_cp0=random_wrist_punch(),
# wrist_cp1=random_wrist_punch(),
# wrist_cp2=random_wrist_punch(),
# wrist_cp3=random_wrist_punch(),
# wrist_cp4=random_wrist_punch(),
# wrist_cp5=random_wrist_punch(),
# wrist_cp6=random_wrist_punch(),
# wrist_cp7=random_wrist_punch(),
# wrist_cp8=random_wrist_punch(),
# wrist_cp9=random_wrist_punch(),
# wrist_cp10=random_wrist_punch(),
# wrist_cp11=random_wrist_punch(),
# wrist_cp12=random_wrist_punch(),
# wrist_cp13=random_wrist_punch(),
# wrist_cp14=random_wrist_punch(),
# wrist_cp15=random_wrist_punch(),
# wrist_cp16=random_wrist_punch(),
# wrist_cp17=random_wrist_punch(),
# wrist_cp18=random_wrist_punch(),
# wrist_cp19=random_wrist_punch(),
# wrist_cp20=random_wrist_punch(),
# wrist_cp21=random_wrist_punch(),
# wrist_cp22=random_wrist_punch(),
# wrist_cp23=random_wrist_punch(),
# wrist_cp24=random_wrist_punch(),
# wrist_cp25=random_wrist_punch(),
# wrist_cp26=random_wrist_punch(),
# wrist_cp27=random_wrist_punch(),
# wrist_cp28=random_wrist_punch(),
# wrist_cp29=random_wrist_punch(),
# wrist_cp30=random_wrist_punch(),
# wrist_cp31=random_wrist_punch(),
# wrist_cp32=random_wrist_punch(),
# wrist_cp33=random_wrist_punch(),
# wrist_cp34=random_wrist_punch(),
# wrist_cp35=random_wrist_punch(),
# wrist_cp36=random_wrist_punch(),
# wrist_cp37=random_wrist_punch(),
# wrist_cp38=random_wrist_punch(),
# wrist_cp39=random_wrist_punch(),
# wrist_cp40=random_wrist_punch(),
# wrist_cp41=random_wrist_punch(),
# wrist_cp42=random_wrist_punch(),
# wrist_cp43=random_wrist_punch(),
# wrist_cp44=random_wrist_punch(),
# wrist_cp45=random_wrist_punch(),
# wrist_cp46=random_wrist_punch(),
# wrist_cp47=random_wrist_punch(),
# wrist_cp48=random_wrist_punch(),
# wrist_cp49=random_wrist_punch(),
# wrist_cp50=random_wrist_punch(),
# wrist_cp51=random_wrist_punch(),
# wrist_cp52=random_wrist_punch(),
# wrist_cp53=random_wrist_punch(),
# wrist_cp54=random_wrist_punch(),
# wrist_cp55=random_wrist_punch(),
# wrist_cp56=random_wrist_punch(),
# wrist_cp57=random_wrist_punch(),
# wrist_cp58=random_wrist_punch(),
# wrist_cp59=random_wrist_punch(),
# wrist_cp60=random_wrist_punch(),
# wrist_cp61=random_wrist_punch(),
# wrist_cp62=random_wrist_punch(),
# wrist_cp63=random_wrist_punch(),
# wrist_cp64=random_wrist_punch(),
# wrist_cp65=random_wrist_punch(),
# wrist_cp66=random_wrist_punch(),
# wrist_cp67=random_wrist_punch(),
# wrist_cp68=random_wrist_punch(),
# wrist_cp69=random_wrist_punch(),
# wrist_cp70=random_wrist_punch(),
# wrist_cp71=random_wrist_punch(),
# wrist_cp72=random_wrist_punch(),
# wrist_cp73=random_wrist_punch(),
# wrist_cp74=random_wrist_punch(),
# wrist_cp75=random_wrist_punch(),
# wrist_cp76=random_wrist_punch(),
# wrist_cp77=random_wrist_punch(),
# wrist_cp78=random_wrist_punch(),
# wrist_cp79=random_wrist_punch(),
# wrist_cp80=random_wrist_punch(),
# wrist_cp81=random_wrist_punch(),
# wrist_cp82=random_wrist_punch(),
# wrist_cp83=random_wrist_punch(),
# wrist_cp84=random_wrist_punch(),
# wrist_cp85=random_wrist_punch(),
# wrist_cp86=random_wrist_punch(),
# wrist_cp87=random_wrist_punch(),
# wrist_cp88=random_wrist_punch(),
# wrist_cp89=random_wrist_punch(),
# wrist_cp90=random_wrist_punch(),
# wrist_cp91=random_wrist_punch(),
# wrist_cp92=random_wrist_punch(),
# wrist_cp93=random_wrist_punch(),
# wrist_cp94=random_wrist_punch(),
# wrist_cp95=random_wrist_punch(),
# wrist_cp96=random_wrist_punch(),
# wrist_cp97=random_wrist_punch(),
# wrist_cp98=random_wrist_punch(),
# wrist_cp99=random_wrist_punch(),
# wrist_cp100=random_wrist_punch(),
# wrist_cp101=random_wrist_punch(),
# wrist_cp102=random_wrist_punch(),
# wrist_cp103=random_wrist_punch(),
# wrist_cp104=random_wrist_punch(),
# wrist_cp105=random_wrist_punch(),
# wrist_cp106=random_wrist_punch(),
# wrist_cp107=random_wrist_punch(),
# wrist_cp108=random_wrist_punch(),
# wrist_cp109=random_wrist_punch(),
# wrist_cp110=random_wrist_punch(),
# wrist_cp111=random_wrist_punch(),
# wrist_cp112=random_wrist_punch(),
# wrist_cp113=random_wrist_punch(),
# wrist_cp114=random_wrist_punch(),
# wrist_cp115=random_wrist_punch(),
# wrist_cp116=random_wrist_punch(),
# wrist_cp117=random_wrist_punch(),
# wrist_cp118=random_wrist_punch(),
# wrist_cp119=random_wrist_punch(),
# wrist_cp120=random_wrist_punch(),
# wrist_cp121=random_wrist_punch(),
# wrist_cp122=random_wrist_punch(),
# wrist_cp123=random_wrist_punch(),
# wrist_cp124=random_wrist_punch(),
# wrist_cp125=random_wrist_punch(),
# wrist_cp126=random_wrist_punch(),
# wrist_cp127=random_wrist_punch(),
# wrist_cp128=random_wrist_punch(),
# wrist_cp129=random_wrist_punch(),
# wrist_cp130=random_wrist_punch(),
# wrist_cp131=random_wrist_punch(),
# wrist_cp132=random_wrist_punch(),
# wrist_cp133=random_wrist_punch(),
# wrist_cp134=random_wrist_punch(),
# wrist_cp135=random_wrist_punch(),
# wrist_cp136=random_wrist_punch(),
# wrist_cp137=random_wrist_punch(),
# wrist_cp138=random_wrist_punch(),
# wrist_cp139=random_wrist_punch(),
# wrist_cp140=random_wrist_punch(),
# wrist_cp141=random_wrist_punch(),
# wrist_cp142=random_wrist_punch(),
# wrist_cp143=random_wrist_punch(),
# wrist_cp144=random_wrist_punch(),
# wrist_cp145=random_wrist_punch(),
# wrist_cp146=random_wrist_punch(),
# wrist_cp147=random_wrist_punch(),
# wrist_cp148=random_wrist_punch(),
# wrist_cp149=random_wrist_punch(),
# wrist_cp150=random_wrist_punch(),
# wrist_cp151=random_wrist_punch(),
# wrist_cp152=random_wrist_punch(),
# wrist_cp153=random_wrist_punch(),
# wrist_cp154=random_wrist_punch(),
# wrist_cp155=random_wrist_punch(),
# wrist_cp156=random_wrist_punch(),
# wrist_cp157=random_wrist_punch(),
# wrist_cp158=random_wrist_punch(),
# wrist_cp159=random_wrist_punch(),
# wrist_cp160=random_wrist_punch(),
# wrist_cp161=random_wrist_punch(),
# wrist_cp162=random_wrist_punch(),
# wrist_cp163=random_wrist_punch(),
# wrist_cp164=random_wrist_punch(),
# wrist_cp165=random_wrist_punch(),
# wrist_cp166=random_wrist_punch(),
# wrist_cp167=random_wrist_punch(),
# wrist_cp168=random_wrist_punch(),
# wrist_cp169=random_wrist_punch(),
# wrist_cp170=random_wrist_punch(),
# wrist_cp171=random_wrist_punch(),
# wrist_cp172=random_wrist_punch(),
# wrist_cp173=random_wrist_punch(),
# wrist_cp174=random_wrist_punch(),
# wrist_cp175=random_wrist_punch(),
# wrist_cp176=random_wrist_punch(),
# wrist_cp177=random_wrist_punch(),
# wrist_cp178=random_wrist_punch(),
# wrist_cp179=random_wrist_punch(),
# wrist_cp180=random_wrist_punch(),
# wrist_cp181=random_wrist_punch(),
# wrist_cp182=random_wrist_punch(),
# wrist_cp183=random_wrist_punch(),
# wrist_cp184=random_wrist_punch(),
# wrist_cp185=random_wrist_punch(),
# wrist_cp186=random_wrist_punch(),
# wrist_cp187=random_wrist_punch(),
# wrist_cp188=random_wrist_punch(),
# wrist_cp189=random_wrist_punch(),
# wrist_cp190=random_wrist_punch(),
# wrist_cp191=random_wrist_punch(),
# wrist_cp192=random_wrist_punch(),
# wrist_cp193=random_wrist_punch(),
# wrist_cp194=random_wrist_punch(),
# wrist_cp195=random_wrist_punch(),
# wrist_cp196=random_wrist_punch(),
# wrist_cp197=random_wrist_punch(),
# wrist_cp198=random_wrist_punch(),
# wrist_cp199=random_wrist_punch(),
# wrist_cp200=random_wrist_punch(),
# wrist_cp201=random_wrist_punch(),
# wrist_cp202=random_wrist_punch(),
# wrist_cp203=random_wrist_punch(),
# wrist_cp204=random_wrist_punch(),
# wrist_cp205=random_wrist_punch(),
# wrist_cp206=random_wrist_punch(),
# wrist_cp207=random_wrist_punch(),
# wrist_cp208=random_wrist_punch(),
# wrist_cp209=random_wrist_punch(),
# wrist_cp210=random_wrist_punch(),
# wrist_cp211=random_wrist_punch(),
# wrist_cp212=random_wrist_punch(),
# wrist_cp213=random_wrist_punch(),
# wrist_cp214=random_wrist_punch(),
# wrist_cp215=random_wrist_punch(),
# wrist_cp216=random_wrist_punch(),
# wrist_cp217=random_wrist_punch(),
# wrist_cp218=random_wrist_punch(),
# wrist_cp219=random_wrist_punch(),
# wrist_cp220=random_wrist_punch(),
# wrist_cp221=random_wrist_punch(),
# wrist_cp222=random_wrist_punch(),
# wrist_cp223=random_wrist_punch(),
# wrist_cp224=random_wrist_punch(),
# wrist_cp225=random_wrist_punch(),
# wrist_cp226=random_wrist_punch(),
# wrist_cp227=random_wrist_punch(),
# wrist_cp228=random_wrist_punch(),
# wrist_cp229=random_wrist_punch(),
# wrist_cp230=random_wrist_punch(),
# wrist_cp231=random_wrist_punch(),
# wrist_cp232=random_wrist_punch(),
# wrist_cp233=random_wrist_punch(),
# wrist_cp234=random_wrist_punch(),
# wrist_cp235=random_wrist_punch(),
# wrist_cp236=random_wrist_punch(),
# wrist_cp237=random_wrist_punch(),
# wrist_cp238=random_wrist_punch(),
# wrist_cp239=random_wrist_punch(),
# wrist_cp240=random_wrist_punch(),
# wrist_cp241=random_wrist_punch(),
# wrist_cp242=random_wrist_punch(),
# wrist_cp243=random_wrist_punch(),
# wrist_cp244=random_wrist_punch(),
# wrist_cp245=random_wrist_punch(),
# wrist_cp246=random_wrist_punch(),
# wrist_cp247=random_wrist_punch(),
# wrist_cp248=random_wrist_punch(),
# wrist_cp249=random_wrist_punch(),
# wrist_cp250=random_wrist_punch(),
# wrist_cp251=random_wrist_punch(),
# wrist_cp252=random_wrist_punch(),
# wrist_cp253=random_wrist_punch(),
# wrist_cp254=random_wrist_punch(),
# 'M-12'
# 'M-14'
# 'M-16'
# 'M-18'
# 'M-20'
# 'M-21'
# 'M-21A'
# 'M-21E'
# 'M-35'
# 'M-40'
# 'M-45'
# 'M-50'
# 'M-55'
# 'M-60'
# 'M-65'
# 'M-70'
# 'M-75'
# 'M-80'
# 'M-O'
# 'M-N'
# 'W-12'
# 'W-14'
# 'W-16'
# 'W-18'
# 'W-20'
# 'W-21'
# 'W-21A'
# 'W-21E'
# 'W-35'
# 'W-40'
# 'W-45'
# 'W-50'
# 'W-55'
# 'W-60'
# 'W-65'
# 'W-70'
# 'W-75'
# 'W-80'
# 'W-O'
# 'W-N'

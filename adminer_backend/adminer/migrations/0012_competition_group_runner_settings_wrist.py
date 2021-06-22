# Generated by Django 3.2.3 on 2021-06-18 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adminer', '0011_auto_20210618_2241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_name', models.CharField(max_length=50)),
                ('comp_type', models.PositiveSmallIntegerField()),
                ('comp_data', models.CharField(max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=20)),
                ('group_seq', models.CharField(max_length=200)),
                ('group_competition_id', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Runner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('runner_sn', models.PositiveIntegerField()),
                ('runner_competition_id', models.PositiveSmallIntegerField()),
                ('runner_group_id', models.PositiveIntegerField()),
                ('runner_name', models.CharField(max_length=50)),
                ('runner_club', models.CharField(max_length=30)),
                ('runner_coach', models.CharField(max_length=50)),
                ('runner_skill', models.CharField(max_length=20)),
                ('runner_state', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('printer_ip', models.GenericIPAddressField()),
                ('printer_autoprint', models.BooleanField()),
                ('current_comp_id', models.PositiveSmallIntegerField()),
                ('version', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Wrist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wrist_competition_id', models.PositiveSmallIntegerField()),
                ('wrist_sn', models.PositiveSmallIntegerField()),
                ('wrist_firmware', models.PositiveSmallIntegerField()),
                ('wrist_voltage', models.PositiveSmallIntegerField()),
                ('wrist_passed', models.BooleanField()),
                ('wrist_total_time', models.PositiveIntegerField()),
                ('wrist_points', models.PositiveSmallIntegerField()),
                ('wrist_seq', models.CharField(max_length=1024)),
                ('wrist_punches', models.CharField(max_length=1800)),
            ],
        ),
    ]

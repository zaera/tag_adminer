# Generated by Django 3.2.3 on 2021-06-18 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminer', '0006_settings_printer_autoprint'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Competition',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='Runner',
        ),
        migrations.DeleteModel(
            name='Settings',
        ),
        migrations.DeleteModel(
            name='Wrist',
        ),
    ]

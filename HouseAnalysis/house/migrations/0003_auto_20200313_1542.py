# Generated by Django 2.1.5 on 2020-03-13 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0002_auto_20200313_1448'),
    ]

    operations = [
        migrations.RenameField(
            model_name='constructure',
            old_name='layout',
            new_name='constructure',
        ),
        migrations.RenameField(
            model_name='decortion',
            old_name='layout',
            new_name='decoration',
        ),
        migrations.RenameField(
            model_name='orientation',
            old_name='layout',
            new_name='orientation',
        ),
        migrations.RenameField(
            model_name='purposes',
            old_name='layout',
            new_name='purposes',
        ),
        migrations.RenameField(
            model_name='region',
            old_name='layout',
            new_name='region',
        ),
    ]

# Generated by Django 2.1.5 on 2020-04-17 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0007_auto_20200416_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='rangeIndex',
            field=models.IntegerField(default=1, verbose_name='房价等级'),
            preserve_default=False,
        ),
    ]
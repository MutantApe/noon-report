# Generated by Django 2.2.6 on 2019-10-23 11:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20191023_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 10, 23, 11, 50, 45, 516623, tzinfo=utc), verbose_name='Date'),
        ),
    ]
# Generated by Django 2.2.6 on 2019-10-23 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20191023_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Teacher'),
        ),
    ]

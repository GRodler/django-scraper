# Generated by Django 4.2.4 on 2023-08-06 21:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_alter_user_info_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 8, 6, 21, 58, 31, 883682)),
        ),
    ]

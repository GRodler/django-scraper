# Generated by Django 4.2.4 on 2023-08-06 22:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0004_alter_user_info_age_alter_user_info_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 8, 6, 22, 47, 46, 562482)),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]

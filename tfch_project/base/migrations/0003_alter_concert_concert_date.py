# Generated by Django 4.2 on 2023-05-05 15:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_concert_concert_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concert',
            name='concert_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 5, 17, 0, 11, 615587), unique=True),
        ),
    ]

# Generated by Django 4.2 on 2023-05-05 15:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_concert_concert_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concert',
            name='concert_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 5, 17, 28, 36, 280418)),
        ),
    ]

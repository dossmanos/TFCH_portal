# Generated by Django 4.1.7 on 2023-04-20 22:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_program_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 21, 0, 40, 10, 709000)),
        ),
    ]

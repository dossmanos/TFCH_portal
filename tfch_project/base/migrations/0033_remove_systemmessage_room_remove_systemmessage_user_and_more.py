# Generated by Django 4.1.7 on 2023-04-26 20:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0032_alter_concert_concert_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='systemmessage',
            name='room',
        ),
        migrations.RemoveField(
            model_name='systemmessage',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='program',
            options={'ordering': ['program_pianist']},
        ),
        migrations.AlterField(
            model_name='concert',
            name='concert_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 26, 22, 43, 49, 66389), unique=True),
        ),
        migrations.DeleteModel(
            name='ChatRoom',
        ),
        migrations.DeleteModel(
            name='ChatTopic',
        ),
        migrations.DeleteModel(
            name='SystemMessage',
        ),
    ]

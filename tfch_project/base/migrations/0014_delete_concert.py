# Generated by Django 4.1.7 on 2023-04-14 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_program_name_concert'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Concert',
        ),
    ]
# Generated by Django 4.1.7 on 2023-04-17 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_delete_concert'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pianist',
            name='next_concert',
        ),
        migrations.AddField(
            model_name='program',
            name='concert_date',
            field=models.DateField(null=True),
        ),
    ]
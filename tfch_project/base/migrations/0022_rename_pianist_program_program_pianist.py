# Generated by Django 4.1.7 on 2023-04-20 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_remove_program_pianist_program_pianist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='program',
            old_name='pianist',
            new_name='program_pianist',
        ),
    ]
# Generated by Django 3.1.5 on 2021-02-10 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('progreso', '0002_auto_20210210_2158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='date',
            old_name='apellido',
            new_name='last_name',
        ),
    ]
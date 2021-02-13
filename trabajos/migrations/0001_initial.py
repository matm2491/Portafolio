# Generated by Django 3.1.5 on 2021-02-12 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=400)),
                ('img', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'work',
                'verbose_name_plural': 'works',
            },
        ),
    ]

# Generated by Django 3.0.4 on 2020-04-12 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='database',
            options={'ordering': ['type']},
        ),
    ]

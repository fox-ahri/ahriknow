# Generated by Django 3.0.4 on 2020-04-12 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0008_auto_20200410_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(to='notebook.Tag'),
        ),
    ]
# Generated by Django 3.0.4 on 2020-04-19 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_article_link'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-update']},
        ),
    ]
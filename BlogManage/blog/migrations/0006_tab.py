# Generated by Django 3.0.4 on 2020-04-19 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_category_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tab',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=254)),
                ('index', models.SmallIntegerField(default=1)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'blog_tab',
            },
        ),
    ]

# Generated by Django 3.0.4 on 2020-04-01 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jurisdiction',
            options={},
        ),
        migrations.AddField(
            model_name='jurisdiction',
            name='parent',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='jurisdiction.Jurisdiction'),
        ),
    ]

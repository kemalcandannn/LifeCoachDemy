# Generated by Django 3.0.3 on 2020-06-03 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='state',
            field=models.BooleanField(default=False, verbose_name='Durumu'),
        ),
    ]
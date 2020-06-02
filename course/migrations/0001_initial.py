# Generated by Django 3.0.3 on 2020-06-02 23:25

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Dersin Adı')),
                ('subject', models.CharField(max_length=120, verbose_name='Dersin Konusu')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='İçerik')),
                ('state', models.BooleanField(verbose_name='Durumu')),
                ('slug', models.SlugField(editable=False, max_length=130, unique=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to=settings.AUTH_USER_MODEL, verbose_name='Dersi Veren Kişi')),
            ],
        ),
    ]

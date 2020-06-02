# Generated by Django 3.0.3 on 2020-06-02 18:19

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
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=250, verbose_name='Ad Soyad')),
                ('name', models.CharField(max_length=120, verbose_name='Başlık')),
                ('eMail', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='İçerik')),
                ('slug', models.SlugField(editable=False, max_length=130, unique=True)),
                ('answered', models.BooleanField(default=False, verbose_name='Cevaplanma Durumu')),
                ('post_answered_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Postu Cevaplayan Kişi')),
            ],
        ),
    ]
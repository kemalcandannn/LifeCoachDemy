from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.

class Course(models.Model):
    staff = models.ForeignKey('auth.User', verbose_name='Dersi Veren Kişi', related_name='courses', on_delete=models.CASCADE)
    name = models.CharField(max_length=120, verbose_name='Dersin Adı')
    content = RichTextField(verbose_name='İçerik', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # Buradaki course, course/urls.py dosyasındaki app_name verisi
        return reverse('course:detail', kwargs={'id': self.id})

    def get_create_url(self):
        # Buradaki course, course/urls.py dosyasındaki app_name verisi
        return reverse('course:create')

    def get_update_url(self):
        # Buradaki course, course/urls.py dosyasındaki app_name verisi
        return reverse('course:update', kwargs={'id': self.id})

    def get_delete_url(self):
        # Buradaki course, course/urls.py dosyasındaki app_name verisi
        return reverse('course:delete', kwargs={'id': self.id})

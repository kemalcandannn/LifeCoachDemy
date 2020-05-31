from django.db import models
from django.urls import reverse

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=120, verbose_name='Dersin Adı')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #Buradaki course, course/urls.py dosyasındaki app_name verisi
        return reverse('course:detail', kwargs={'id' : self.id})
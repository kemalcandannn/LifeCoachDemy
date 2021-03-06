from datetime import datetime

from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class User(models.Model):
    user = models.ForeignKey('auth.User', verbose_name='Kullanıcı', related_name='users', on_delete=models.CASCADE)
    name = models.CharField(max_length=150, verbose_name='Ad')
    surname = models.CharField(max_length=150, verbose_name='Soyad')
    register_date = models.DateTimeField(verbose_name='Kayıt Tarihi', editable=False)
    mail = models.EmailField(verbose_name='E-Mail', unique=True)
    cep_tel = models.CharField(max_length=20, null=True, blank=True, unique=True)
    #profession = models.ForeignKey()
    photo = models.ImageField(verbose_name='Fotoğraf', null=True, blank=True)

    #VerilenDersler

    experience = RichTextField(verbose_name='Tecrübe', null=True, blank=True)
    instructor_score = models.IntegerField(verbose_name='Eğitmenlik Puanı',null=True, blank=True)
    total_course_number = models.IntegerField(verbose_name='Şimdiye Kadar Verilen Dersler', default=0)
    current_course_number = models.IntegerField(verbose_name='Güncel Ders Sayısı', default=0)

    slug = models.SlugField(unique=True, editable=False, max_length=130)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('user:detail', kwargs={'slug': self.slug})

    def get_create_url(self):
        return reverse('user:create')

    def get_update_url(self):
        return reverse('user:update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('user:delete', kwargs={'slug': self.slug})

    def get_unique_slug(self):
        slug = slugify(self.name.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while User.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}_{}'.format(slug, counter)
            counter += 1

        return unique_slug

    def save(self, *args, **kwargs):
        if not self.id:
            self.register_date = datetime.now()
        self.slug = self.get_unique_slug()
        return super(User, self).save(*args, **kwargs)

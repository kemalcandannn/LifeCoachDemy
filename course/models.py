from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# Create your models here.

class Course(models.Model):
    staff = models.ForeignKey('auth.User', verbose_name='Dersi Veren Kişi', related_name='courses', on_delete=models.CASCADE)
    name = models.CharField(max_length=120, verbose_name='Dersin Adı')
    content = RichTextField(verbose_name='İçerik', null=True, blank=True)
    slug = models.SlugField(unique=True, editable=False, max_length=130)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # Buradaki course, course/urls.py dosyasındaki app_name verisi
        return reverse('course:detail', kwargs={'slug': self.slug})

    def get_create_url(self):
        # Buradaki course, course/urls.py dosyasındaki app_name verisi
        return reverse('course:create')

    def get_update_url(self):
        # Buradaki course, course/urls.py dosyasındaki app_name verisi
        return reverse('course:update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        # Buradaki course, course/urls.py dosyasındaki app_name verisi
        return reverse('course:delete', kwargs={'slug': self.slug})

    def get_unique_slug(self):
        slug = slugify(self.name.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Course.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}_{}'.format(slug, counter)
            counter += 1

        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Course, self).save(*args, **kwargs)



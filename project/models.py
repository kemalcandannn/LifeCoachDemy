from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# Create your models here.

class Project(models.Model):
    project_owner = models.ForeignKey('auth.User', verbose_name='Proje Sahibi', related_name='projects', on_delete=models.CASCADE)
    name = models.CharField(max_length=120, verbose_name='Projenin Adı')
    content = RichTextField(verbose_name='İçerik', null=True, blank=True)
    slug = models.SlugField(unique=True, editable=False, max_length=130)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # Buradaki project, project/urls.py dosyasındaki app_name verisi
        return reverse('project:detail', kwargs={'slug': self.slug})

    def get_create_url(self):
        # Buradaki course, course/urls.py dosyasındaki app_name verisi
        return reverse('project:create')

    def get_update_url(self):
        # Buradaki project, project/urls.py dosyasındaki app_name verisi
        return reverse('project:update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        # Buradaki project, project/urls.py dosyasındaki app_name verisi
        return reverse('project:delete', kwargs={'slug': self.slug})

    def get_unique_slug(self):
        slug = slugify(self.name.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Project.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}_{}'.format(slug, counter)
            counter += 1

        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Project, self).save(*args, **kwargs)



from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# Create your models here.

class Contact(models.Model):
    post_owner = models.ForeignKey('auth.User', verbose_name='Postun Sahibi', related_name='contacts', on_delete=models.CASCADE)
    name = models.CharField(max_length=120, verbose_name='Başlık')
    eMail = models.EmailField(verbose_name='E-mail')
    content = RichTextField(verbose_name='İçerik', null=True, blank=True)
    slug = models.SlugField(unique=True, editable=False, max_length=130)
    post_answered_user = models.ForeignKey('auth.User', verbose_name='Postu Cevaplayan Kişi', on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contacts:detail', kwargs={'slug': self.slug})

    def get_create_url(self):
        return reverse('contacts:create')

    def get_update_url(self):
        return reverse('contacts:update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('contacts:delete', kwargs={'slug': self.slug})

    def get_unique_slug(self):
        slug = slugify(self.name.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Contact.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}_{}'.format(slug, counter)
            counter += 1

        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Contact, self).save(*args, **kwargs)

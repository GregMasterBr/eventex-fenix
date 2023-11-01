from django.db import models
from eventex.subscriptions.validators import validate_cpf
from django.shortcuts import resolve_url as r

# Create your models here.
class Speaker(models.Model):
    name = models.CharField('nome',max_length=255)
    title = models.CharField('título',max_length=100)
    slug = models.SlugField('slug')
    photo = models.URLField('foto')
    website = models.URLField('website', blank=True)
    description = models.TextField('descrição', blank=True)
    created_at = models.DateTimeField('criado em',auto_now=True)

    class Meta:
        verbose_name_plural = 'palestrantes'
        verbose_name = 'palestrante'
        #ordering = ('-created_at',)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('speaker_detail', slug=self.slug)
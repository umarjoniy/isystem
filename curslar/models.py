from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


class Courses(models.Model):
    title = models.CharField(max_length=150, verbose_name='имя')
    month = models.IntegerField(default=0)
    day = models.IntegerField(default=0)
    price = models.IntegerField()
    description = models.TextField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True,null=True,unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Kurs'
        verbose_name_plural = 'Kurslar'

@receiver(pre_save, sender = Courses)
def article_pre_save(sender,instance,*args,**kwargs):
    instance.slug = slugify(instance.title)


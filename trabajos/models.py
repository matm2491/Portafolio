from django.db import models

# Create your models here.


class Work(models.Model):

    title = models.CharField(max_length=40, blank=False)
    description = models.CharField(max_length=400, blank=False)
    img = models.ImageField(upload_to= 'working')

    class Meta:
        verbose_name='work'
        verbose_name_plural='works'

    def __str__(self):

        return self.title

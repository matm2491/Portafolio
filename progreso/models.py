from django.db import models

# Create your models here.

class Date(models.Model):
    
    name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    comments=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='date'
        verbose_name_plural='dates'

    def __str__(self):
        return self.title

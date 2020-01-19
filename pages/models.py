from django.db import models

# Create your models here.


class HomeClass(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    picture = models.ImageField(upload_to='pages/%Y/%m/%d/')

    def __str__(self):
        return self.title
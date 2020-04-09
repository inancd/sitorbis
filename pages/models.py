from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class HomeClass(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    picture = models.ImageField(upload_to='pages/%Y/%m/%d/')

    def __str__(self):
        return self.title

class TermClass(models.Model):
    title = models.CharField(max_length=120)
    context = RichTextUploadingField()

    def __str__(self):
        return self.title

class PrivacyClass(models.Model):
    title = models.CharField(max_length=120)
    context = RichTextUploadingField()

    def __str__(self):
        return self.title


class StatementClass(models.Model):
    title = models.CharField(max_length=120)
    context = RichTextUploadingField()

    def __str__(self):
        return self.title
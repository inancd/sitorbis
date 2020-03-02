from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save, post_delete
from django.utils.text import slugify
from django.conf import settings
from django.dispatch import receiver
from django.urls import reverse

class PostCategory(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, unique=True, max_length=400)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

def pre_save_post_category_receiever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
pre_save.connect(pre_save_post_category_receiever, sender=PostCategory)


class Post(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True, max_length=400)
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='post_likes')
    text = RichTextField()
    dated_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='blog/%Y/%m/%d/')
    editor_featured = models.BooleanField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})


def pre_save_post_receiever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

pre_save.connect(pre_save_post_receiever, sender=Post)



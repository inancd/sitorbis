from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

from sitorbis.utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.urls import reverse

User = get_user_model()

# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:catdetail', kwargs={'slug': self.slug})

def save_title_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(save_title_slug, sender=Category)



class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True, null=True)
    body = RichTextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='media/news/%Y/%m/%d/')
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()
    slider_accept = models.BooleanField()
    def __str__(self):
        return self.title


def save_title_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(save_title_slug, sender=News)









from django.contrib.sitemaps import Sitemap
from blog.models import Post

class BlogSitemap(Sitemap):
    daily = 0.5
    protocol = "https"

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.dated_posted

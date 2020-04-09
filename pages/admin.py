from django.contrib import admin

from .models import HomeClass, PrivacyClass, TermClass,StatementClass

# Register your models here.

admin.site.register(HomeClass)
admin.site.register(PrivacyClass)
admin.site.register(TermClass)
admin.site.register(StatementClass)

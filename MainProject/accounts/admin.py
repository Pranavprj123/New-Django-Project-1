from django.contrib import admin
from .models import *
# Register your models here.
#@admindecorator
admin.site.register([Contributor,Address])
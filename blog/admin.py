from django.contrib import admin
from .models import *
from tinymce.widgets import TinyMCE
# Register your models here.


admin.site.register(Article)
admin.site.register(Author)


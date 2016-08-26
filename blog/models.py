from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.encoding import python_2_unicode_compatible
from blog.choices import *
from tinymce import models as tinymce_models

# Create your models here.

class Author(models.Model):
	name = models.CharField(max_length=50)
	
	def __unicode__(self):
		return u'%s' % self.name
	pass

class Article(models.Model):
	author = models.ForeignKey(Author)
	title = models.CharField(max_length=200)
	created = models.DateTimeField(auto_now_add=True)
	status = models.IntegerField(choices=STATUS_CHOICES, default=2)
	content = tinymce_models.HTMLField()
	description = tinymce_models.HTMLField()
	image = models.ImageField()
	
	def __unicode__(self):
		return u'%s' % self.title
	pass
	

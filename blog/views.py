from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.urlresolvers import reverse
from .forms import *
from django.core.mail import send_mail

# Create your views here.

def index(request):
	articles = Article.objects.all()
	block = {
	'articles':articles
	}
	return render(request, 'index.html', block)
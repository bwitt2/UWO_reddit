from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from UWO_reddit.models import *
def index(request):
	ls = Post
	template = loader.get_template('UWO_reddit_app/index.html')
	context = RequestContext(request, {
		'posts' : ls,
		})
	return HttpResponse(template.render(context))


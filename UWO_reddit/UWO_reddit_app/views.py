from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from UWO_reddit_app.models import *


def index(request):
    ls = Post.objects.all()
    template = loader.get_template('UWO_reddit_app/index.html')
    context = RequestContext(request, {'posts': ls, })
    return HttpResponse(template.render(context))


def display(request, primary_key):
	template = loader.get_template('UWO_reddit_app/display.html')
	context = RequestContext(request, {
		})
	return HttpResponse()


def display(request, primary_key):
    template = loader.get_template('UWO_reddit_app/display.html')
    context = RequestContext(request, {
        })
    return HttpResponse()

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from campuscollabapp.models import *


def index(request):
    ls = Post.objects.all()
    template = loader.get_template('campuscollabapp/index.html')
    context = RequestContext(request, {'posts': ls, })
    return HttpResponse(template.render(context))


def display(request, primary_key):

    template = loader.get_template('campuscollabapp/display.html')
    context = RequestContext(request, {
        })
    return HttpResponse("Currently viewing Category with Primary Key: " + primary_key)

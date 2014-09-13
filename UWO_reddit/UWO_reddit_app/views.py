from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

def main(request):
	template = loader.get_template()


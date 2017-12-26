from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    template = loader.get_template('landing/index.html')
    context = {'title': 'Advize Yourself'}
    return HttpResponse(template.render(context, request))

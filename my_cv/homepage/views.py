from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def cv(request):
    template = loader.get_template('cv.html')
    return HttpResponse(template.render())

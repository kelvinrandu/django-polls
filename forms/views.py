from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Form


# Create your views here.
def index(request):
    template = loader.get_template('forms/index.html')
    response = Form.objects.all()
    context = {
        'response_list': response,
    }
    return HttpResponse(template.render(context, request))

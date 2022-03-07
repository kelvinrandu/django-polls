from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import CreateView
from .forms import FormForm
from django.views import generic

from .models import Form


class CreatePersona(generic.FormView):
    model = Form
    form_class = FormForm
    template_name = 'forms/create.html'

# # Create your views here.
def index(request):
    template = loader.get_template('forms/index.html')
    response = Form.objects.all()
    context = {
        'response_list': response,
    }
    return HttpResponse(template.render(context, request))

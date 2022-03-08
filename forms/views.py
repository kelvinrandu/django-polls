from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic import CreateView
from .forms import FormForm
from django.views import generic
from django.urls import reverse_lazy

from .models import Form


class CreatePersona(generic.FormView):
    model = Form
    form_class = FormForm
    success_url = '/forms/create'

    template_name = 'forms/create.html'
    # context = {
    #     'form': form_class,
    # }


# # Create your views here.
def index(request):
    template = loader.get_template('forms/index.html')
    response = Form.objects.all()
    context = {
        'response_list': response,
    }
    return HttpResponse(template.render(context, request))

from django.shortcuts import render,redirect
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
    success_url = '/forms'

    template_name = 'forms/create.html'
    # context = {
    #     'form': form_class,
    # }
def create(request):
    form = FormForm()
    if request.method == 'POST':
        form = FormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/forms')
    template = loader.get_template('forms/create.html')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))

# # Create your views here.
def index(request):
    template = loader.get_template('forms/index.html')
    response = Form.objects.all()
    context = {
        'response_list': response,
    }
    return HttpResponse(template.render(context, request))

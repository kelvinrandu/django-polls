from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic import CreateView
from .forms import FormForm
from django.views import generic
from django.core.mail import send_mail

from .models import Form


class CreatePersona(generic.FormView):
    model = Form
    form_class = FormForm
    template_name = 'forms/create.html'


def get_name(request):
    template = loader.get_template('forms/create.html')
    context = {
        'response_list': 'response',
    }

    

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FormForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            subject = form.cleaned_data['name']
            message = form.cleaned_data['address']
            sender = form.cleaned_data['email']
            recipients = ['info@example.com']

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/forms')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FormForm()
        response = Form.objects.all()
        context = {
        'response_list': response,
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

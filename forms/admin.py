from django.contrib import admin
from .models import Form
from django import forms

# Register your models here.
class FormForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = "__all__"

admin.site.register(Form)

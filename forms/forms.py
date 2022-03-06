from django import forms
from forms.models import Form


class FormForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = [
            "name",
            "email",
            "address",
            "computer_literate",
            "income",
            "years_of_experience",

        ]

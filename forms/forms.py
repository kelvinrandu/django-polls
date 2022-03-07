from django import forms
from forms.models import Form
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


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
        required_fields = (
        'name',
        'email',
 
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save persona'))



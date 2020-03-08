from django import forms


class SubjectForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=200, required=True)

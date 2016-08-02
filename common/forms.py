from django import forms


class CreateForm(forms.Form):
    id = forms.CharField(label='id', max_length=20)
    pw = forms.CharField(label='pw', max_length=30)

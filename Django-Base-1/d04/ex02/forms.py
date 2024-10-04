from django import forms

class MyForm(forms.Form):
    text_field = forms.CharField(label='Entrez du texte', max_length=100)

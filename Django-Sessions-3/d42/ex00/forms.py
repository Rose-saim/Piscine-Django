# ex00/forms.py
from django import forms
from .models import Tip

class TipForm(forms.ModelForm):
    class Meta:
        model = Tip
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Entrez votre astuce ici...', 'rows': 4}),
        }

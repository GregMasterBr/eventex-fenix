from django.core.exceptions import ValidationError
from django import forms

class SubscriptionForm(forms.Form):
    name = forms.CharField(label='Nome')
    cpf = forms.CharField(label='CPF')
    email = forms.EmailField(label='E-mail')
    phone = forms.CharField(label='Telefone')

    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     words = [w.capitalize() for w in name.split()]
    #     return ' '.join(words)

    # def clean(self):
    #     if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
    #         raise ValidationError('Informe seu e-mail ou telefone.')

    #     return self.cleaned_data
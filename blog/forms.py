from django import forms
from .models import *


class FeedBackForm(forms.Form):
    name = forms.CharField(max_length=50, label='Ваше имя:', required=True, min_length=3,  error_messages={'max_length': 'Это поле не должно превышать 50 симоволов', 'min_length': 'Ввведите ваше имя', 'required': 'Это поле обязательное'})
    phone = forms.CharField(max_length=18, label='Телефон:', min_length=18, required=True, error_messages={'min_length': 'Заполните номер правильно'})
    addr = forms.CharField(max_length=50, label='Адрес:', required=True,  error_messages={'max_length': 'Это поле не должно превышать 50 символов'})

    def __init__(self, *args, **kwargs):
        super(FeedBackForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {'id': 'first_name', 'class': 'fio',
                                                  'placeholder': 'Ваше имя', 'max_length': '50'}
        self.fields['phone'].widget.attrs = {'id': 'phone', 'class': 'tel',
                                             'placeholder': 'Ваш номер телефона',
                                             'data-tel-input': '', 'max_length': '18', 'min_length': '18'}
        self.fields['addr'].widget.attrs = {'id': 'addr', 'class': 'addr',
                                                  'placeholder': 'Ваш Адрес', }

    def clean_name(self, *args, **kwargs):
        name = self.cleaned_data.get('name')

        if name == '':
            raise forms.ValidationError('Заполните это поле для продолжения')

        else:
            return name

    def clean_phone(self, *args, **kwargs):
        phone = self.cleaned_data.get('phone]')


        if phone == '':
            raise forms.ValidationError('Заполните это поле для продолжения')

        else:
            print(phone)
            return phone

    def clean_addr(self, *args, **kwargs):
        addr = self.cleaned_data.get('addr')

        if addr == '':
            raise forms.ValidationError('Заполните это поле для продолжения')

        else:
            return addr

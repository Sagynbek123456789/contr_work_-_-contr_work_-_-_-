from django import forms
from webapp.models import status_choices


class TaskForm(forms.Form):
    author = forms.CharField(max_length=60, required=True, label='автор')
    mail = forms.EmailField(max_length=70, required=True, label='почта')
    description = forms.CharField(max_length=50, required=True, label='описание')
    # status = forms.ChoiceField(choices=status_choices, label='Статус')


class AuthorSearchForm(forms.Form):
    author = forms.CharField(label='Имя автора', max_length=60)

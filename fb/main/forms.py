from django import forms

from django.forms import ModelForm

from main.models import *


class IncomeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['amount'].label = "Сумма"
        self.fields['desc'].label = "Описание"
        self.fields['date'].label = "Дата"

    class Meta:
        model = Income
        fields = ['amount', 'desc', 'date']

class ExpenseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['amount'].label = "Сумма"
        self.fields['desc'].label = "Описание"
        self.fields['date'].label = "Дата"
        
    class Meta:
        model = Expense
        fields = ['amount', 'desc', 'date']

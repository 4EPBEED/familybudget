from django import forms

from django.forms import ModelForm

from main.models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class IncomeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['amount'].label = "Сумма"
        self.fields['desc'].label = "Описание"
        self.fields['date'].label = "Дата"
        self.fields['incomeSource'].label = "Источник дохода"
        self.fields['familyMember'].label = "Член семьи"

    class Meta:
        model = Income
        fields = ['amount', 'incomeSource', 'familyMember', 'desc', 'date']

        widgets = {
            'date': DateInput(),
        }

class ExpenseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['amount'].label = "Сумма"
        self.fields['desc'].label = "Описание"
        self.fields['date'].label = "Дата"
        self.fields['expenseSource'].label = "Источник расхода"
        self.fields['familyMember'].label = "Член семьи"
        
    class Meta:
        model = Expense
        fields = ['amount', 'expenseSource', 'familyMember', 'desc', 'date']

        widgets = {
            'date': DateInput(),
        }

class IncomeSourceForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Название источника"

    class Meta:
        model = IncomeSource
        fields = ['title']

class ExpenseSourceForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Название источника"

    class Meta:
        model = ExpenseSource
        fields = ['title']

class FamilyMemberForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Имя"
        self.fields['age'].label = "Возраст"

    class Meta:
        model = FamilyMember
        fields = ['name', 'age']

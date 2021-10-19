from django.shortcuts import redirect, render

from main.forms import *
from main.models import *

# Create your views here.
def index(request):
    incomes = Income.objects.all()
    expenses = Expense.objects.all()

    return render(request, 'index.html', {"incomes": incomes, "expenses": expenses, 
                                            'incomeForm': IncomeForm, 'expenseForm': ExpenseForm})

def incomeCreate(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

def expenseCreate(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
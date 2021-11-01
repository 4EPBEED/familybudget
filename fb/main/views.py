from datetime import datetime

from django.shortcuts import redirect, render
from django.db.models import Sum, Value as V, FloatField
from django.db.models.functions import Coalesce

from main.forms import *
from main.models import *

months = {
    "январь": 1,
    "февраль": 2,
    "март": 3,
    "апрель": 4,
    "май": 5,
    "июнь": 6,
    "июль": 7,
    "август": 8,
    "сентябрь": 9,
    "октябрь": 10,
    "ноябрь": 11,
    "декабрь": 12,
}

# Create your views here.
def index(request):
    incomes = Income.objects.all().order_by('-date')
    expenses = Expense.objects.all().order_by('-date')

    monthsTotal = [0 for i in range(1, 13)]

    currentYear = datetime.today().year
    currentMonth = datetime.today().month

    for i in range(1, 13):
        monthIncomes = incomes.filter(date__month=i, date__year=currentYear)
        monthExpense = expenses.filter(date__month=i, date__year=currentYear)

        monthTotalIncome = monthIncomes.aggregate(sum=Coalesce(Sum('amount'), V(0.0)))
        monthTotalExpense = monthExpense.aggregate(sum=Coalesce(Sum('amount'), V(0.0)))
        

        monthsTotal[i - 1] = monthTotalIncome["sum"] - monthTotalExpense["sum"]

    return render(request, 'index.html', {"incomes": incomes, "expenses": expenses, 
                                            'incomeForm': IncomeForm, 'expenseForm': ExpenseForm,
                                            'incomeSourceForm': IncomeSourceForm, 'expenseSourceForm': ExpenseSourceForm,
                                            'familyMemberForm': FamilyMemberForm,
                                            'monthsTotal': monthsTotal, 'currentMonth': currentMonth})

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

def incomeSourceCreate(request):
    if request.method == 'POST':
        form = IncomeSourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

def expenseSourceCreate(request):
    if request.method == 'POST':
        form = ExpenseSourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

def familyMemberCreate(request):
    if request.method == 'POST':
        form = FamilyMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
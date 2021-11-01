from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("income/create", views.incomeCreate, name='income-create'),
    path("expense/create", views.expenseCreate, name='expense-create'),
    path("income/source/create", views.incomeSourceCreate, name='income-source-create'),
    path("expense/source/create", views.expenseSourceCreate, name='income-source-create'),
]

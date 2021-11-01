from django.contrib import admin
from main.models import *

# Register your models here.
admin.site.register(Income)
admin.site.register(Expense)
admin.site.register(IncomeSource)
admin.site.register(ExpenseSource)
admin.site.register(FamilyMember)
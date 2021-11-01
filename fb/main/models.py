from django.db import models
from django.db.models.expressions import Value

# Create your models here.
class FamilyMember(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

class IncomeSource(models.Model):
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % self.title

class Income(models.Model):
    amount = models.FloatField()
    desc = models.CharField(max_length=200)
    date = models.DateField()
    familyMember = models.ForeignKey(FamilyMember,
                                    on_delete=models.CASCADE,
                                    blank=True,
                                    null=True)
    incomeSource = models.ForeignKey(IncomeSource,
                                    on_delete=models.CASCADE,
                                    blank=True,
                                    null=True)

class ExpenseSource(models.Model):
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % self.title

class Expense(models.Model):
    amount = models.FloatField()
    desc = models.CharField(max_length=200)
    date = models.DateField()
    familyMember = models.ForeignKey(FamilyMember,
                                    on_delete=models.CASCADE,
                                    blank=True,
                                    null=True)
    expenseSource = models.ForeignKey(ExpenseSource,
                                    on_delete=models.CASCADE,
                                    blank=True,
                                    null=True)



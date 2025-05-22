from django.shortcuts import render
from .forms import ExpenseForm
from .models import Expense
from django.utils import timezone
from datetime import timedelta

def add_expense(request):
    form = ExpenseForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'tracker/add_expense.html', {'form': form})

def view_expenses(request, name):
    if name == 'all':
        expenses = Expense.objects.all()
        name = "Barcha foydalanuvchilar"
    else:
        expenses = Expense.objects.filter(name=name)
    return render(request, 'tracker/view_expenses.html', {'expenses': expenses, 'name': name})


def weekly_expenses(request, name):
    today = timezone.now()
    one_week_ago = today - timedelta(days=7)

    if name == 'all':
        expenses = Expense.objects.filter(date__gte=one_week_ago)
        name = "Barcha foydalanuvchilar (so‘nggi 7 kun)"
    else:
        expenses = Expense.objects.filter(name=name, date__gte=one_week_ago)

    return render(request, 'tracker/view_expenses.html', {'expenses': expenses, 'name': name})



def filter_expenses(request, name, period):
    now = timezone.now().date()

    if period == "week":
        start_date = now - timedelta(days=7)
    elif period == "month":
        start_date = now.replace(day=1)
    elif period == "year":
        start_date = now.replace(month=1, day=1)
    else:
        start_date = None

    if start_date:
        expenses = Expense.objects.filter(name=name, date__gte=start_date)
    else:
        expenses = Expense.objects.filter(name=name)

    return render(request, 'tracker/view_expenses.html', {'expenses': expenses, 'name': name})

def home(request):
    users = Expense.objects.values_list('name', flat=True).distinct()
    return render(request, 'tracker/home.html', {'users': users})

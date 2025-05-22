from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_expense, name='add_expense'),
    path('expenses/<str:name>/', views.view_expenses, name='view_expenses'),
    path('expenses/<str:name>/week/', views.weekly_expenses, name='weekly_expenses'),
    path('expenses/<str:name>/month/', views.filter_expenses, {'period': 'month'}, name='monthly_expenses'),
    path('expenses/<str:name>/year/', views.filter_expenses, {'period': 'year'}, name='yearly_expenses'),
]

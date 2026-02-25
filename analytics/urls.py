from django.urls import path
from .views import MonthlySummaryView, IncomeExpenseView, CategoryBreakdownView

urlpatterns = [
    path('monthly-summary/', MonthlySummaryView.as_view()),
    path('income-vs-expense/',IncomeExpenseView.as_view()),
    path('category-breakdown/',CategoryBreakdownView.as_view()),

]

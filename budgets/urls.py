from rest_framework.routers import DefaultRouter
from .views import BudgetViewSet, BudgetStatusView
from django.urls import path

router = DefaultRouter()
router.register(r'', BudgetViewSet, basename='budgets')

urlpatterns = [
    path('status/', BudgetStatusView.as_view()),
]

urlpatterns += router.urls

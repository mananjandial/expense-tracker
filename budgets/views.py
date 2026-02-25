from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Budget
from .serializers import BudgetSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from transactions.models import Transaction


class BudgetViewSet(ModelViewSet):
    serializer_class = BudgetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class BudgetStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        year = int(request.query_params.get("year"))
        month = int(request.query_params.get("month"))
        category = request.query_params.get("category")

        budget = Budget.objects.filter(
            user=request.user,
            year=year,
            month=month,
            category=category
        ).first()

        if not budget:
            return Response({"message": "No budget found"}, status=404)

        spent = Transaction.objects.filter(
            user=request.user,
            date__year=year,
            date__month=month,
            category=category,
            type="expense"
        ).aggregate(total=Sum("amount"))["total"] or 0

        remaining = budget.amount - spent
        percentage_used = (spent / budget.amount) * 100 if budget.amount > 0 else 0

        return Response({
            "budget": budget.amount,
            "spent": spent,
            "remaining": remaining,
            "percentage_used": round(percentage_used, 2)
        })

# Create your views here.

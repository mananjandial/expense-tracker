from django.db.models import Sum
from django.utils.timezone import now
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from transactions.models import Transaction
from datetime import datetime
from core.utils import success_response, error_response


class MonthlySummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        year = int(request.query_params.get("year", now().year))
        month = int(request.query_params.get("month", now().month))

        transactions = Transaction.objects.filter(
            user=request.user,
            date__year=year,
            date__month=month
        )

        income = transactions.filter(type="income").aggregate(
            total=Sum("amount")
        )["total"] or 0

        expense = transactions.filter(type="expense").aggregate(
            total=Sum("amount")
        )["total"] or 0

        savings = income - expense

        return success_response(
            data={
                "year": year,
                "month": month,
                "income": income,
                "expense": expense,
                "savings": savings
            },
            message="Monthly summary fetched successfully"
        )


        #     return Response({
        #     "year": year,
        #     "month": month,
        #     "income": income,
        #     "expense": expense,
        #     "savings": savings
        # })
class IncomeExpenseView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        year = int(request.query_params.get("year", now().year))
        month = int(request.query_params.get("month", now().month))

        transactions = Transaction.objects.filter(
            user=request.user,
            date__year=year,
            date__month=month
        )

        income = transactions.filter(type="income").aggregate(
            total=Sum("amount")
        )["total"] or 0

        expense = transactions.filter(type="expense").aggregate(
            total=Sum("amount")
        )["total"] or 0

        return Response({
            "income": income,
            "expense": expense
        })

# Create your views here.
from django.db.models import Sum


class CategoryBreakdownView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        year = int(request.query_params.get("year", now().year))
        month = int(request.query_params.get("month", now().month))
        txn_type = request.query_params.get("type", "expense")

        transactions = (
            Transaction.objects
            .filter(
                user=request.user,
                date__year=year,
                date__month=month,
                type=txn_type
            )
            .values("category")
            .annotate(total=Sum("amount"))
            .order_by("-total")
        )

        return Response(transactions)

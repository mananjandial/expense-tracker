from django.urls import path
from .views import dashboard, login_view

urlpatterns = [
    path('', dashboard),
    path('login/', login_view),
]
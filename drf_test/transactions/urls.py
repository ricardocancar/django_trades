from django.urls import path, include
from rest_framework.routers import DefaultRouter
from transactions.views import TransactionsViewSet, TransactionsListView, UsersViewSet, BankAccountViewSet, CreditCardSViewSet

router = DefaultRouter()
router.register(r'transactions', TransactionsViewSet, basename='transactions')
router.register(r'users', UsersViewSet)
router.register(r'bank-accounts', BankAccountViewSet)
router.register(r'credit-cards', CreditCardSViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('transactions-list', TransactionsListView.as_view(), name='transactions-list')
]
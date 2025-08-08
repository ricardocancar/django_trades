from rest_framework import viewsets, generics, permissions
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from .models import Transactions, Users, BankAccount, CreditCard
from .serializers import TransactionsSerializers, UsersSerializers, BankAccountSerializers, CreditCardSerializers


class TransactionsViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionsSerializers
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    def get_queryset(self):
        user_email = getattr(self.request.user, "email", None)
        if not user_email:
            return Transactions.objects.none()
        try:
            user = Users.objects.get(email=user_email)
        except Users.DoesNotExist:
            return Transactions.objects.none()
        return Transactions.objects.filter(user_id=user)


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializers


class BankAccountViewSet(viewsets.ModelViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializers


class CreditCardSViewSet(viewsets.ModelViewSet):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializers



class TransactionsListView(generics.ListAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializers

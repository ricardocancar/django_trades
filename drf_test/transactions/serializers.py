from rest_framework import serializers
from transactions.models import Transactions, Users, BankAccount, CreditCard


class TransactionsSerializers(serializers.ModelSerializer):
    """
    Serializer for the Transactions model.

    This serializer automatically includes all fields from the Transactions model.
    It is used to convert model instances to and from native Python datatypes
    suitable for rendering into JSON, XML, or other content types.

    Attributes:
        Meta (class): Configuration for the serializer, specifying the model and fields to include.
    """
    class Meta:
        model = Transactions
        fields= '__all__'


class UsersSerializers(serializers.ModelSerializer):
    """"""
    class Meta:
        model = Users
        fields = '__all__'

class BankAccountSerializers(serializers.ModelSerializer):
    """"""
    class Meta:
        model = BankAccount
        fields = '__all__'

class CreditCardSerializers(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = '__all__'
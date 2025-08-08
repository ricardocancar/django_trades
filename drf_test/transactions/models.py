import uuid
from django.db import models
from cryptography.fernet import Fernet

FERNET_KEY = b'v1Jv9wQw7kQ7n6w3Q1v9wQw7kQ7n6w3Q1v9wQw7kQ7n='  # "some random text in base64"
fernet = Fernet(FERNET_KEY)


class Transactions(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('Users', on_delete=models.SET_NULL, null=True, related_name='transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    state = models.CharField(max_length=20, default='pending')
    account_id =  models.ForeignKey('BankAccount', on_delete=models.SET_NULL, null=True)
    card_id = models.ForeignKey('CreditCard', on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    create_at = models.DateField(auto_now_add=True)


class BankAccount(models.Model):
    id = models.AutoField(primary_key=True)
    iban = models.CharField(
        max_length=36,
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
    bank = models.CharField(max_length=30)

class CreditCard(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=255)
    def save(self, *args, **kwargs):
        # Encrypt only if not already encrypted (simple check)
        if not self.number.startswith('gAAAA'):
            self.number = fernet.encrypt(self.number.encode()).decode()
        super().save(*args, **kwargs)

    @property
    def decrypted_number(self):
        return fernet.decrypt(self.number.encode()).decode()
    BRAND_CHOICES = [
        ('visa', 'Visa'),
        ('mastercard', 'Mastercard'),
        ('amex', 'American Express'),
        # Add more brands as needed
    ]
    brand = models.CharField(max_length=20, choices=BRAND_CHOICES)
    end_date = models.DateField()
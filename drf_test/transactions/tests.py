from datetime import date

from django.test import TestCase

from .models import CreditCard


class CreditCardModelTest(TestCase):
    def test_credit_card_number_encrypted_and_decrypted(self):
        original_number = "4111111111111111"

        card = CreditCard.objects.create(
            number=original_number,
            brand="visa",
            end_date=date(2030, 1, 1),
        )

        # The stored number should be encrypted and differ from the original
        self.assertNotEqual(card.number, original_number)

        # decrypted_number should return the original number
        self.assertEqual(card.decrypted_number, original_number)

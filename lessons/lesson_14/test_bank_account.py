import unittest
from decimal import Decimal

from faker import Faker
from random import randint, choice

from helpers.helpers import assert_logged
from lessons.lesson_14.bank_account import BankAccount

fake = Faker()


class TestBankAccount(unittest.TestCase):

    def test_bank_account_init(self):
        """
        Test bank_account initialization
        """
        test_owner = fake.name()
        test_init_balance = choice([0, randint(1, 100)])
        test_currency = choice(BankAccount.SUPPORTED_CURRENCY)

        bank_account = BankAccount(test_owner, test_init_balance, test_currency)

        for expected_attr in ["owner", "currency", "_active", "_balance"]:
            assert_logged(hasattr(bank_account, expected_attr))

        assert_logged(all([
            bank_account.owner == test_owner,
            bank_account.get_balance() == test_init_balance,
            bank_account.currency == test_currency,
            bank_account._active,
            bank_account.__dict__ == {'owner': test_owner, '_balance': test_init_balance, 'currency': test_currency, 'transaction_history': [], '_active': True}
            ]))


    def test_bank_account_transfer_success(self):
        """
        Test verifies transfer operation succeed
        """
        init_balance_1 = randint(1, 100)
        init_balance_2 = randint(1, 30)

        bank_account_1 = BankAccount(fake.name(), init_balance_1, "EUR")
        bank_account_2 = BankAccount(fake.name(), init_balance_2, "EUR")

        amount = randint(1, init_balance_1)

        bank_account_1.transfer_to(receiver=bank_account_2, amount=amount)

        assert_logged(bank_account_1.get_balance() == init_balance_1 - amount, f"Bank_account_1 balance expected to be {init_balance_1 - amount} but actually got {bank_account_1.get_balance()}")
        assert_logged(bank_account_2.get_balance() == init_balance_2 + amount, f"Bank_account_2 balance expected to be {init_balance_2 - amount} but actually got {bank_account_1.get_balance()}")

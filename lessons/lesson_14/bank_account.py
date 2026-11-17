import datetime
from decimal import Decimal
from typing import Optional, Self

from lessons.lesson_14.bank_account_exceptions import InsufficientFundsError, CurrencyMismatchError, \
    IsActiveAccountError, InActiveAccountError, BaseBankAccountError
# logger

class BankAccount:
    SUPPORTED_CURRENCY = ["USD", "EUR", "UAH"]

    def __init__(self, owner: str, initial_balance: int | float, currency: str):
        if not isinstance(owner, str) or not bool(owner):
            raise ValueError("Please enter a valid owner")
        if currency.upper() not in self.SUPPORTED_CURRENCY:
            raise ValueError("Please enter a valid currency code")
        self.owner: str = owner
        self._balance: Decimal = self._validate_amount(amount=initial_balance)
        self.currency: str = currency
        self.transaction_history: list[dict] = []
        self._active = True

    def __str__(self):
        return f"{self.__dict__}"

    def __repr__(self):
        return f"{self.__dict__}"

    def _validate_amount(self, amount: int | float | Decimal, min_limit=0) -> Optional[Decimal]:
        if type(amount) not in (int, float, Decimal):
            raise ValueError("Please enter a valid amount")
        if amount < min_limit:
            raise ValueError(f"Amount cannot be less than {min_limit}")
        return Decimal(amount)

    def _record_transaction(self, amount: Decimal, tran_type: str, receiver: Optional[Self] = None) -> None:
        timestamp = datetime.datetime.now().timestamp()
        tran_record = {
            "amount": amount,
            "tran_type": tran_type,
            "timestamp": timestamp,
            "balance_after": self._balance,
        }
        if receiver:
            tran_record["receiver"] = receiver
        self.transaction_history.append(tran_record)

    def get_balance(self) -> Decimal:
        return self._balance

    def balance_top_up(self, amount: Decimal) -> Decimal:
        if not self._active:
            raise InActiveAccountError("Account is inactive")
        self._validate_amount(amount, min_limit=1)
        self._balance += amount
        self._record_transaction(amount, "top_up")
        return self._balance

    def withdraw(self, amount: Decimal) -> Decimal:
        if not self._active:
            raise InActiveAccountError("Account is inactive")
        self._validate_amount(amount, min_limit=1)
        if amount > self._balance:
            raise InsufficientFundsError(f"Failed to withdraw {amount} from {self.owner}. Available: {self._balance}")
        self._balance -= amount
        self._record_transaction(amount, "withdrawal")
        return self._balance

    def transfer_to(self, receiver: Self, amount: Decimal):

        if not all([self._active, receiver._active]):
            raise InActiveAccountError("Some of the accounts are inactive")

        if self.currency != receiver.currency:
            raise CurrencyMismatchError(f"Currency mismatch: {receiver.currency} and {self.currency}")
        self._validate_amount(amount, min_limit=1)

        balance_before = self._balance
        receiver_balance = receiver.get_balance()
        try:
            self.withdraw(amount)
            receiver.balance_top_up(amount)
        except BaseBankAccountError as e:
            # rollback
            self._balance = balance_before
            receiver._balance = receiver_balance
            raise e
        finally:
            self._record_transaction(amount, "transfer_to", receiver)

    def deactivate_account(self):
        self._active = False

    def activate_account(self):
        if self._active is True:
            raise IsActiveAccountError("Account is already active")
        self._active = True

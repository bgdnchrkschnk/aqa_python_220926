class BaseBankAccountError(Exception):
    """
    Exceptions related to bank account errors.
    """




class InsufficientFundsError(BaseBankAccountError):
    """
    Raised when a bank account has insufficient funds.
    """

class CurrencyMismatchError(BaseBankAccountError):
    """
    Raised when sender/receiver's currency are not the same.
    """

class IsActiveAccountError(BaseBankAccountError):
    """
    Raised when account is already active.
    """

class InActiveAccountError(BaseBankAccountError):
    """
    Raised when an account is inactive.
    """
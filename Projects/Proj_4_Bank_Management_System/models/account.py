"""
account.py — Account hierarchy using OOP Inheritance & Polymorphism.
 
Classes:
    Account            — base class
    SavingsAccount     — 4% interest, ₹500 min balance
    CheckingAccount    — no interest, ₹10,000 overdraft allowed
    FixedDepositAccount— 7.5% interest, no withdrawals
"""

import uuid
from datetime import datetime 
from database.db_manager import DatabaseManager

# ====================================================================== #
#  Base Account                                                            #
# ====================================================================== #

class Account:
    """Base class for all bank accounts."""
    ACCOUNT_TYPES = "base"
    DEFAULT_INTREST_RATE = 0.0
    MIN_BALANCE = 0.0

    def __init__(self , customer_id: str, balance: float = 0.0 , account_number: str = None , status: str = "active" , intrest_rate: float = None , created_at: str = None,):
        self.account_number = account_number or self._gen_acc_no()
        self.customer_id = customer_id
        self.balance = round(balance, 2)
        self.status = status
        self.intrest_rate = intrest_rate if intrest_rate is not None else self.DEFAULT_INTREST_RATE
        self.created_at = created_at or datetime.now().isoformat()

    # -------------------------------------------------------------- #
    #  Private guards                                                  #
    # -------------------------------------------------------------- #

    def _gen_acc_no(self) -> str: 
        """Generate a unique account number."""
        return f"ACC{uuid.uuid4().int % 10**10 :010d}"
    
    def _check_active(self):
        if self.status != "active":
            raise PermissionError(f"Account {self.account_number} is '{self.status}'- Operation not allowed.")
        
    def _check_amount(self , amount: float):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        


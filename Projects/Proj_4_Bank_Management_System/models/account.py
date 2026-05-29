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
        

    # -------------------------------------------------------------- #
    #  Core operations (overridden in subclasses)                     #
    # -------------------------------------------------------------- #

    def deposit(self, amount: float , descripttion: str = "Deposit"):
        """Deposit money into the account."""
        self._check_active()
        self._check_amount(amount)
        self.balance += round(amount, 2)
        txn = self.save_transaction("deposite" , amount , descripttion)
        self._update_db()
        return txn  
    
    def withdraw(self, amount: float , descripttion: str = "Withdrawal") -> dict:
        """Withdraw money from the account."""
        self._check_active()
        self._check_amount(amount)
        if self.balance - amount < self.MIN_BALANCE:
            raise ValueError(f"Insufficient funds. Minimum balance of ₹{self.MIN_BALANCE} must be maintained.")
        self.balance -= round(amount, 2)
        txn = self.save_transaction("withdrawal" , amount , descripttion)
        self._update_db()
        return txn
    
    def apply_interest(self):
        """Apply interest to the account balance."""
        self._check_active()
        if self.intrest_rate <=0 :
            raise ValueError("This account does not earn interest.")
        interest = round(self.balance * (self.intrest_rate / 100), 2)
        self.balance += round(interest, 2)
        txn = self.save_tranction("interest", interest, f"Interest @ {self.interest_rate}%")
        self._update_db()
        return txn
    
    def get_statement(self , limit : int = 10) -> list:
        """Get the account statement (last N transactions)."""
        db = DatabaseManager()
        with db.get_connection() as conn:
            rows = conn.execute("""
                SELECT * FROM transactions WHERE account_number = ? ORDER BY timestamp DESC LIMIT ?
            """, (self.account_number, limit)).fetchall()

        return [dict(row) for row in rows]
    
    def freeze(self):
        """Freeze the account (no transactions allowed)."""
        self.status = "frozen"
        self._update_db()
        DatabaseManager().log_action("FREEZE" , "account" , self.account_number)


    def close(self):
        self.status = "closed"
        self._update_db()
        DatabaseManager().log_action("CLOSE" , "account" , self.account_number)

    # -------------------------------------------------------------- #
    #  DB helpers                                                      #
    # -------------------------------------------------------------- #

    def _save_transaction(self , txn_type: str , amount: float , description: str) -> dict:
        """Save a transaction to the database."""
        txn_id = f"TXN{uuid.uuid4().hex[:8].upper()}"
        
        db = DatabaseManager()
        with db.get_connection() as conn:
            conn.execute("""
                INSERT INTO transactions (transaction_id, account_number, txn_type, amount, balance_after ,  description, timestamp)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (txn_id, self.account_number, txn_type, amount, self.balance,  description, datetime.now().isoformat()))

        return {
            "transaction_id": txn_id,
            "account_number": self.account_number,
            "type": txn_type,
            "amount": amount,
            "balance_after": self.balance,
            "description": description,
            "timestamp": datetime.now().isoformat()
        }
    

    def _update_db(self):
        """Update the account details in the database."""
        db = DatabaseManager()
        with db.get_connection() as conn:
            conn.execute("""
                UPDATE accounts SET balance = ?, status = ? WHERE account_number = ?
            """, (self.balance, self.status, self.account_number))

    # -------------------------------------------------------------- #
    #  Class-level finders                                             #
    # -------------------------------------------------------------- #

    @classmethod
    def _from_row(cls , row) -> "Account":
        """Factory — returns the correct subclass based on account_type."""
        mapping = {
            "savings": SavingsAccount,
            "checking": CheckingAccount,
            "fixed_deposit": FixedDepositAccount
        }

        klass = mapping.get(row["account_type"], cls)

        return klass(
            customer_id=row["customer_id"],
            balance=row["balance"],
            account_number=row["account_number"],
            status=row["status"],
            intrest_rate=row["intrest_rate"],
            created_at=row["created_at"]
        )

    @classmethod
    def find_by_number(cls , account_number: str):
        """Find an account by its number."""
        db = DatabaseManager()
        with db.get_connection() as conn:
            row = conn.execute("""
                SELECT * FROM accounts WHERE account_number = ?
            """, (account_number,)).fetchone()

        return cls._from_row(row) if row else None

    @classmethod
    def find_by_customer(cls , customer_id: str) -> list:
        """Find all accounts for a given customer."""
        db = DatabaseManager()
        with db.get_connection() as conn:
            rows = conn.execute("""
                SELECT * FROM accounts WHERE customer_id = ? ORDER BY created_at 
            """, (customer_id,)).fetchall()

        return [cls._from_row(row) for row in rows]
    

    def __repr__(self):
        return (
            f"<{self.__class__.__name__} account_number={self.account_number} "
            f"customer_id={self.customer_id} balance=₹{self.balance:.2f} status={self.status}>"
        )
    
class SavingsAccount(Account):
    ACCOUNT_TYPES = "savings"
    DEFAULT_INTREST_RATE = 4.0
    MIN_BALANCE = 500.0

    def withdraw(self, amount: float , descripttion: str = "Withdrawal") -> dict:
        """Withdraw money from the savings account."""
        self._check_active()
        self._check_amount(amount)
        if self.balance - amount < self.MIN_BALANCE:
            raise ValueError(f"Insufficient funds. Minimum balance of ₹{self.MIN_BALANCE} must be maintained.")
        self.balance -= round(amount, 2)
        txn = self._save_transaction("withdrawal" , amount , descripttion)
        self._update_db()
        return txn
    

class CheckingAccount(Account):
    ACCOUNT_TYPES = "checking"
    DEFAULT_INTREST_RATE = 0.0
    MIN_BALANCE = -10000.0  # Overdraft allowed up to ₹10,000

    def withdraw(self, amount: float , descripttion: str = "Withdrawal") -> dict:
        """Withdraw money from the checking account."""
        self._check_active()
        self._check_amount(amount)
        if self.balance - amount < self.MIN_BALANCE:
            raise ValueError(f"Overdraft limit exceeded. You can overdraft up to ₹{-self.MIN_BALANCE}.")
        self.balance -= round(amount, 2)
        txn = self._save_transaction("withdrawal" , amount , descripttion)
        self._update_db()
        return txn
    
class FixedDepositAccount(Account):
    ACCOUNT_TYPES = "fixed_deposit"
    DEFAULT_INTREST_RATE = 7.5
    MIN_BALANCE = 0.0

    def withdraw(self, amount: float , descripttion: str = "Withdrawal") -> dict:
        """Withdrawals are not allowed from fixed deposit accounts."""
        raise PermissionError("Withdrawals are not allowed on Fixed Deposit accounts before maturity. "
            "Please visit your branch to prematurely close the FD.")
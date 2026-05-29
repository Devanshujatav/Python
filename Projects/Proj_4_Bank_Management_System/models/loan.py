import uuid
import math
from datetime import datetime
from database.db_manager import DatabaseManager

# ====================================================================== #
"""Represents a bank loan with monthly EMI repayment."""
def __init__(self, customer_id: str, account_number: str ,  principal: float, intrest_rate: float, tenure_months: int, loan_id: str = None, outstanding:float = None, status: str =  "active", disbursed_at: str = None):
    self.loan_id = loan_id or f"LOAN{uuid.uuid4().hex[:8].upper()}",
    self.customer_id = customer_id
    self.account_number = account_number
    self.principal = round(principal, 2)
    self.intrest_rate = intrest_rate
    self.tenure_months = tenure_months
    self.emi = self._calc_emi()
    self.outstanding = outstanding if outstanding is not None else self.principal
    self.status = status
    self.disbursed_at = disbursed_at or datetime.now().isoformat()

    

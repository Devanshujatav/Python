import uuid
import math
from datetime import datetime
from database.db_manager import DatabaseManager

class Loan:
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

        def _calc_emi(self) -> float:
            r = self.intrest_rate / (12 * 100)  # Monthly interest rate
            n = self.tenure_months
            if r == 0:  # No interest case
                return round(self.principal / n, 2)
            
            emi = self.principal * r * math.pow(1 + r, n) / (math.pow(1 + r, n) - 1)
            return round(emi, 2)
        
        @property
        def total_payable(self) -> float:
            return round(self.emi * self.tenure_months, 2)
        
        @property
        def total_interest(self) -> float:
            return round(self.total_payable - self.principal, 2)
        
        # -------------------------------------------------------------- #
        #  Repayment                                                       #
        # -------------------------------------------------------------- #
        def pay_emi(self) -> dict:
            if self.status != "active":
                raise PermissionError(f"Loan {self.loan_id} is already '{self.status}'.")
            
            payment = round(min(self.emi, self.outstanding), 2)
            self.outstanding = round(self.outstanding - payment, 2)
            if self.outstanding <= 0:
                self.outstanding = 0.0
                self.status = "closed"

            self._update_db()
            DatabaseManager().log("EMI_PAID" , "LOAN" , self.loan_id , f"paid = {payment} outstanding = {self.outstanding}")

            return {
                "loan_id": self.loan_id,
                "payment": payment,
                "outstanding": self.outstanding,
                "status": self.status
            }
        
        # -------------------------------------------------------------- #
        #  Persistence                                                     #
        # -------------------------------------------------------------- #
        def save(self) -> bool: 
            db = DatabaseManager()
            sql = """INSERT INTO loans (loan_id, customer_id, account_number, principal, intrest_rate, tenure_months, emi, outstanding, status, disbursed_at) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ON CONFLICT(loan_id) DO UPDATE SET outstanding=excluded.outstanding, status=excluded.status"""
            
            with db.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql, (self.loan_id, self.customer_id, self.account_number, self.principal, self.intrest_rate, self.tenure_months, self.emi, self.outstanding, self.status, self.disbursed_at))
                
                db.log("LOAN_SAVED" , "LOAN" , self.loan_id , f"principal = {self.principal}")

            return True
        
        def _update_db(self):
            db = DatabaseManager()
            sql = """UPDATE loans SET outstanding = ?, status = ? WHERE loan_id = ?"""
            
            with db.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql, (self.outstanding, self.status, self.loan_id))


        
        # -------------------------------------------------------------- #
        #  Finders                                                         #
        # -------------------------------------------------------------- #
    
        @classmethod
        def _from_row(cls, row) -> "Loan":
            return cls(
                loan_id=row["loan_id"],
                customer_id=row["customer_id"],
                account_number=row["account_number"],
                principal=row["principal"],
                intrest_rate=row["intrest_rate"],
                tenure_months=row["tenure_months"],
                outstanding=row["outstanding"],
                status=row["status"],
                disbursed_at=row["disbursed_at"]
            )
        
        @classmethod
        def find_by_id(cls, loan_id: str):
            db = DatabaseManager()
            sql = "SELECT * FROM loans WHERE loan_id = ?"
            
            with db.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql, (loan_id,))
                row = cursor.fetchone()
                if row:
                    return cls._from_row(row)
                else:
                    raise ValueError(f"Loan with ID {loan_id} not found.")

        @classmethod
        def find_by_customer(cls , customer_id: str):
            db = DatabaseManager()
            with db.get_connection() as conn:
                rows = conn.execute("SELECT * FROM loans WHERE customer_id = ?", (customer_id,)).fetchall()

            return [cls._from_row(row) for row in rows]    
        

        def __repr__(self):
            return (
            f"<Loan {self.loan_id} | ₹{self.principal:,.2f} @ {self.interest_rate}% "
            f"| EMI ₹{self.emi:,.2f} | Outstanding ₹{self.outstanding:,.2f} | {self.status}>"   
        )

        
            

import uuid
from datetime import datetime
from database.db_manager import DatabaseManager
import hashlib

"""Represents a bank customer."""
class Customer:
    def __init__(self , full_name: str,
                    email: str, 
                    phone: str, 
                    pin: str ,
                    address: str = "" , 
                    date_of_birth: str = "" , 
                    customer_id: str = None ,
                    created_at: str = None , 
                    is_active: int = 1):
        
        self.customer_id = customer_id or f"CUST{uuid.uuid4().hex[:8].upper()}"
        self.full_name = full_name,
        self.email = email,
        self.phone = phone,
        self.address = address,
        self.date_of_birth = date_of_birth,
        self.pin_hash = pin if len(pin) == 64 else self._hash(pin)
        self.created_at = created_at or datetime.now().isoformat()
        self.isactive = is_active

    # -------------------------------------------------------------- #
    #  Private helpers                                                 #
    # -------------------------------------------------------------- #
    @staticmethod
    def _hash(pin: str) -> str: 
        """Hash the PIN using SHA-256."""
        return hashlib.sha256(pin.encode()).hexdigest()
    
    # -------------------------------------------------------------- #
    #  Public methods                                                  #
    # -------------------------------------------------------------- #
    
    def verify_pin(self , pin: str) -> bool: 
        """Return True if the given PIN matches the stored hash."""
        return self.pin_hash == self._hash(pin)
    
    def save(self): 
        """Insert or update this customer in the database."""
        db = DatabaseManager()
        sql = """
        INSERT INTO customers (customer_id, full_name, email, phone, address, date_of_birth, pin_hash, created_at, is_active)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(customer_id) DO UPDATE SET
            full_name=excluded.full_name,
            email=excluded.email,
            phone=excluded.phone,
            address=excluded.address,
            is_active=excluded.is_active;
        """
        with db.get_connection() as conn:
            conn.execute(sql, (self.customer_id, self.full_name, self.email, self.phone, self.address, self.date_of_birth, self.pin_hash, self.created_at, self.isactive))

        db.log("save" , "customer" , self.customer_id , self.full_name)

        return True
    
    def deactivate(self):
        db = DatabaseManager()
        with db.get_connection() as conn: 
            conn.execute("UPDATE customers SET is_active = 0 WHERE customer_id = ?", (self.customer_id))

        self.isactive = 0
        db.log("deactivate" , "customer" , self.customer_id , self.full_name)
    
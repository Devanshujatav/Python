import sqlite3
import os
from contextlib import contextmanager

DB_PATH = os.path.join(os.path.dirname(__file__), "..", 'bank.db')

class DatabaseManager: 
    
    """Singleton database manager."""

    _instance = None
    def __new__(cls):
        if cls._instance is None : 
            cls._instance = super().__new__(cls)
            cls._instance._initialize = False
        return cls._instance
    
    def __init__(self):
        if self._instance:
            return
        self.db_path = os.path.abspath(DB_PATH)
        self._instance._initialize = True
        self._create_tables()

    # -------------------------------------------------------------- #
    #  Connection                                                      #
    # -------------------------------------------------------------- #
    @contextmanager
    def get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        try:
            yield conn
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()
        
    # -------------------------------------------------------------- #
    #  Schema                                                          #
    # -------------------------------------------------------------- #
    def _create_tables(self):
        schema = """
        CREATE TABLE IF NOT EXISTS customers (
            customer_id   TEXT PRIMARY KEY,
            full_name     TEXT NOT NULL,
            email         TEXT UNIQUE NOT NULL,
            phone         TEXT NOT NULL,
            address       TEXT DEFAULT '',
            date_of_birth TEXT DEFAULT '',
            pin_hash      TEXT NOT NULL,
            created_at    TEXT DEFAULT (datetime('now')),
            is_active     INTEGER DEFAULT 1
        );
 
        CREATE TABLE IF NOT EXISTS accounts (
            account_number TEXT PRIMARY KEY,
            customer_id    TEXT NOT NULL,
            account_type   TEXT NOT NULL
                               CHECK(account_type IN ('savings','checking','fixed_deposit')),
            balance        REAL NOT NULL DEFAULT 0.0,
            interest_rate  REAL DEFAULT 0.0,
            status         TEXT DEFAULT 'active'
                               CHECK(status IN ('active','frozen','closed')),
            created_at     TEXT DEFAULT (datetime('now')),
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        );
 
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id TEXT PRIMARY KEY,
            account_number TEXT NOT NULL,
            txn_type       TEXT NOT NULL
                               CHECK(txn_type IN ('deposit','withdrawal','transfer','interest')),
            amount         REAL NOT NULL,
            balance_after  REAL NOT NULL,
            description    TEXT DEFAULT '',
            timestamp      TEXT DEFAULT (datetime('now')),
            FOREIGN KEY (account_number) REFERENCES accounts(account_number)
        );
 
        CREATE TABLE IF NOT EXISTS loans (
            loan_id        TEXT PRIMARY KEY,
            customer_id    TEXT NOT NULL,
            account_number TEXT NOT NULL,
            principal      REAL NOT NULL,
            interest_rate  REAL NOT NULL,
            tenure_months  INTEGER NOT NULL,
            emi            REAL NOT NULL,
            outstanding    REAL NOT NULL,
            status         TEXT DEFAULT 'active'
                               CHECK(status IN ('active','closed')),
            disbursed_at   TEXT DEFAULT (datetime('now')),
            FOREIGN KEY (customer_id)    REFERENCES customers(customer_id),
            FOREIGN KEY (account_number) REFERENCES accounts(account_number)
        );
 
        CREATE TABLE IF NOT EXISTS audit_log (
            log_id    INTEGER PRIMARY KEY AUTOINCREMENT,
            action    TEXT NOT NULL,
            entity    TEXT NOT NULL,
            entity_id TEXT,
            details   TEXT,
            timestamp TEXT DEFAULT (datetime('now'))
        );
        """

        with self.get_connection() as conn:
            conn.executescript(schema)

    def log(self , action : str , entity : str , entity_id : str = "" , details : str = "" ):
        sql = "INSERT INTO audit_log (action, entity, entity_id, details) VALUES (?, ?, ?, ?)"
        with self.get_connection() as conn :
            conn.execute(sql , (action , entity , entity_id , details))
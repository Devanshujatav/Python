class Account:
    rupee_symbol = "\u20B9"
    def __init__(self , accountNo , balance):
        self.accountNo = accountNo
        self.balance = balance

    def debit(self , debit_balance):

        self.balance = self.balance - debit_balance
        print(f"The Amount {self.rupee_symbol}{debit_balance} is Debited from Account Number {self.accountNo}")

    def credit(self , credit_balance):
        self.balance = self.balance + credit_balance
        print(f"The Amount {self.rupee_symbol}{credit_balance} is Credited in Account Number {self.accountNo}")

    def remaining_balance(self):
        print(f"The Total Current Amount was",self.rupee_symbol,self.balance)

account1 = Account(6788675769735967 , 1200)
debited = account1.credit(200)
remaining_balance = account1.remaining_balance()
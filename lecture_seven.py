class account:
    def __init__(self,balance,acc):
        self.balance = balance
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("BDT",amount,"was debited.")
        print("Total balance = " ,self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("BDT", amount, "was credited.")
        print("Total balance = ", self.get_balance())
        

    def get_balance(self):
        return self.balance  

acc1 = account(10000,3000)
acc1.debit(1000)
acc1.credit(500)              
acc1.credit(20000)
acc1.debit(5000)
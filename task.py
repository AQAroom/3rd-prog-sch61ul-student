class BankAccount:
  
    def __init__(self, number, sum):
        self.account_number = number
        self.balance = sum
        self.status()
        
    def status(self):
        print(f"Баланс счёта: {self.balance} единиц")
     
    def add(self, sum):
        self.balance = self.balance + sum
        print(f"На счет зачислено: {sum} единиц")
         
    def withdraw(self, sum):
        if self.balance >= sum: 
            self.balance = self.balance - sum
            print(f"Со счета снято: {sum} единиц")
        else:
            print("Недостаточно средств на счете")

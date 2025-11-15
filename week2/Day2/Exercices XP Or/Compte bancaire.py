class BankAccount:
    def __init__(self , balance):
        self.balance = balance
    def deposit(self , valeur):
        if valeur > 0 :
            self.balance += valeur
        else :
           raise ValueError("la valeur doit étre positif")
    def withdraw(self,valeur):
        if valeur > 0 :
            self.balance -= valeur
        else:
            raise ValueError("la valeur doit étre positif")
class MinimumBalanceAccount(BankAccount):
    def __init__(self , minimum_balance = 0 , balance = 0):
        super().__init__(balance)
        self.minimum_balance = minimum_balance
    def withdraw(self , valeur):
        if self.balance - valeur <=  self.minimum_balance :
            self.minimum_balance -= valeur
        else :
            raise ValueError(f"  la valeur balancereste supérieure à la valeur limite minimum_balance,")

acc=BankAccount(200)
print(f"votre balance est : {acc.balance}")
acc.deposit(10)
print(acc.balance)
acc.withdraw(20)
print(acc.balance)
acc1= MinimumBalanceAccount(balance=100, minimum_balance=50)
acc1.withdraw(50)
print(acc1.balance)


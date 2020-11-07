import datetime
import pytz

##
class Account:
    """ Simple account to log all transactions of the funds """

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self.show_total = balance
        self._transaction_list = [(Account._current_time(), balance)]
        print("Account created for " + self._name)
        self.show_balance()
##        self.show_expenses()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("The amount must be greater than zero and no more than your account balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:1} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))

##    def show_total(self, amount):
##        for date, amount in self._transaction_list:
##            #while amount > 0:
##            if amount > 0:
##                tran_type = "deposited"
##                return tran_type.sum()
##                print("Total contribution is", sum)

##    def show_expenses(self):
##         for date, amount in self._transaction_list:
##             amount *= -1
##             tran_type = "withdrawn"
##             sum += tran_type
##             print("Total expenses is", sum)

if __name__ == '__main__':
    simeon = Account("Simeon", 0)

    simeon.deposit(100) # contribution from SB
    simeon.deposit(50)  # contribution from BO
    simeon.withdraw(64.82)  # withdrawal
    simeon.deposit(10)  # contribution from MW
    simeon.deposit(40)  # contribution from DJ
    simeon.withdraw(64.82)  # withdrawal
    simeon.deposit(30)  # contribution from TO
    simeon.deposit(45)  # contribution from FE
    simeon.deposit(35)  # contribution from GO
    simeon.deposit(30)  # contribution from JO
    simeon.withdraw(60)  # withdrawal
    simeon.deposit(32.79)  # contributions from PA,JO, TI
    simeon.deposit(10)  # contribution from A&R A
    simeon.deposit(50)  # contribution from MW
    simeon.withdraw(54.66)  # withdrawal
    simeon.withdraw(72.92)  # withdrawal
    simeon.deposit(10)  # contribution from IS
    simeon.withdraw(23.69)  # withdrawal
    simeon.deposit(30)  # contribution from AS
    simeon.withdraw(50)  # withdrawal
    simeon.withdraw(50)  # withdrawal
    simeon.deposit(30)  # contribution from FI
    simeon.deposit(39)  # contribution from HE
    simeon.withdraw(40)  # withdrawal
    simeon.withdraw(20)  # withdrawal
    simeon.show_transactions()
##    simeon.show_total()    
##    simeon.show_expenses()

contributions = [4.68, 100, 50, 10, 40, 30, 45, 35, 30, 32.79, 10, 50, 10, 30, 30, 39]

expenses = [64.82, 64.82, 60, 54.66, 72.92, 23.69, 50, 50, 40, 20]

Total_contribution = sum(contributions)

Total_expenses = sum(expenses)

Balance = Total_contribution - Total_expenses

print(Total_contribution)

print(Total_expenses)

print(Balance)
    
    





            
            

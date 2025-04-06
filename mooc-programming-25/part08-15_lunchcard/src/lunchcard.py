class LunchCard:   
    def __init__(self, balance: float):
        self.balance = balance
        self.balance_rounded = balance
    def __str__(self):
        self.balance_rounded = format(self.balance,'.1f')
        return f"The balance is {self.balance_rounded} euros"
    def eat_lunch(self):
        if self.balance >= 2.6:
            self.balance -= 2.6
        else:
            pass
    def eat_special(self):
        if self.balance >= 4.6:
            self.balance -= 4.6
        else:
            pass
    def deposit_money(self, deposit: int):
        self.deposit = deposit
        if self.deposit >= 0:
            self.balance += self.deposit
        else: 
            raise ValueError('You cannot deposit an amount of money less than zero.')


  
peters_card = LunchCard(20)
graces_card = LunchCard(30)
peters_card.eat_special()
graces_card.eat_lunch()
print(f"Peter: {peters_card}")
print(f"Grace: {graces_card}")
peters_card.deposit_money(20)
graces_card.eat_special()
print(f"Peter: {peters_card}")
print(f"Grace: {graces_card}")
peters_card.eat_lunch()
peters_card.eat_lunch()
graces_card.deposit_money(50)
print(f"Peter: {peters_card}")
print(f"Grace: {graces_card}")
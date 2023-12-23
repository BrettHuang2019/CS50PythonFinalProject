

class Wallet:
    def __init__(self, startbalance):
        if startbalance>=0:
            self._balance = startbalance
        else:
            raise ValueError("Invalid start balance")

    def __str__(self):
        return f"${self.balance:.2f}"

    @property
    def balance(self):
        return self._balance
    
    def spend(self, price):
        if self.balance >= price: 
            self._balance -=price
        else:
            raise ValueError("Not enough balance")

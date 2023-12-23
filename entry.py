import re
import codecs

class Entry:
    def __init__(self, id, emoji, price, startamount):
        self.id = id
        self.emoji = emoji
        self.price = price
        self.amount = startamount

    def __str__(self):
        if self.amount > 1:
            s = f"{self.emoji} x {self.amount} : ${self.price}/pcs"
        elif self.amount ==1:
            original_price_str = " $"+str(self.price*2) 
            price = ''.join([char+'\u0336' for char in original_price_str])
            s = f"{self.emoji} x {self.amount} :{price}  ${self.price}/pcs"
        return s
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, str):
        if m := re.search(r"^\w+$",str):
            self._id = str
        else:
            raise ValueError("Invalid id.")
        
    @property
    def emoji(self):
        return codecs.decode(self._emoji, 'unicode-escape')
    
    @emoji.setter
    def emoji(self, emojiStr):
        if m := re.search(r"^\\U0001F[0-9][0-F]{2}$",emojiStr.upper()):
            self._emoji = emojiStr.upper()
        else:
            raise ValueError("Invalid emoji unicode.")
    
    @property
    def price(self):
        if self.amount == 1:
            return self._price / 2
        else:
            return self._price

    @price.setter
    def price(self, p):
        if p>0:
            self._price =p
        else:
            raise ValueError("Invalid price.")
        
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, n):
        if n>0:
            self._amount =n
        else:
            raise ValueError("Invalid amount.")
    
    def remove(self, n):
        if self.amount >= n:
            self._amount -= n
        else:
            raise ValueError(f"Insufficient {self._id} to remove.")
        


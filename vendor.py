
class Vendor:
    def __init__(self, entrylist):
        self.entrylist = entrylist

    @property
    def entrylist(self):
        return self._entrylist

    @entrylist.setter
    def entrylist(self, entrylist):
        if len(entrylist) >0:
            self._entrylist = entrylist
        else:
            raise ValueError("Entry list must have at least one element.")
    
    @property
    def is_soldout(self):
        return all(entry.amount<=0 for entry in self.entrylist)

    def sell(self, index):
        if index ==0:
            return False
        sell_entry = self.entrylist[index -1]
        try:
            sell_entry.remove(1)
        except ValueError:
            return False
        return True
                
    def get_available_entries_str(self):
        return [[i+1,str(entry)] for i,entry in enumerate(self.entrylist) if entry.amount>0]
    
    def get_available_entries_indexes(self):
        return [i+1 for i,entry in enumerate(self.entrylist) if entry.amount>0]

    def get_avaliable_free_indexes(self, buy_index):
        buy_entry = self.entrylist[buy_index -1]
        if buy_entry.is_discount:
            return [i+1 for i, entry in enumerate(self.entrylist) if entry.amount>0 and entry.is_discount and entry.price<buy_entry.price]
        else:
            return [i+1 for i, entry in enumerate(self.entrylist) if entry.amount>0 and entry.price<buy_entry.price]
    
    def get_price_by_index(self, index):
        return self.entrylist[index -1].price
    
    def get_cheapest_price(self):
        return min(entry.price for entry in self.entrylist)
    
    def get_emoji_by_index(self, index):
        return  self.entrylist[index -1].emoji

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

    def sell(self, entryid):
        for entry in self.entrylist:
            if entry.id == entryid:
                try:
                    entry.remove(1)
                except ValueError:
                    return False
        return True
                
    def get_available_entries(self):
        return [entry for entry in self.entrylist if entry.amount>0]
    

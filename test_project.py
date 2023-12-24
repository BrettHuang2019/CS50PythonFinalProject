from entry import Entry
from vendor import Vendor
from wallet import Wallet
from project import validate_user_name, validate_index, init_vendor_machine
import pytest

def main():
    test_validate_user_name()
    test_entry()
    test_vendor()
    test_wallet()

def test_validate_user_name():
    assert validate_user_name("abc") == "abc"
    assert validate_user_name("t") == "t"
    assert validate_user_name("123") == "123"
    assert validate_user_name("") == False
    assert validate_user_name("  ") == False
    assert validate_user_name("a  b") == False

def test_validate_index():
    assert validate_index(1, [1,2,3]) == True
    assert validate_index(0, [1,2,3]) == True
    assert validate_index(4, [1,2,3]) == False

def test_init_vendor_machine():
    v = init_vendor_machine()
    assert v != None
    assert len(v.entrylist) == 4

def test_entry():
    e = Entry("hamburger","\\U0001F354",10,2)
    assert e.id == "hamburger"
    assert e.emoji == "🍔"
    assert e.price == 10
    assert str(e) == "🍔 x 2 : $10/pcs"
    e.remove(1)
    assert e.price ==5
    assert str(e) == "🍔 x 1 : ̶$̶1̶0̶.̶0̶  $5.0/pcs"
    with pytest.raises(ValueError):
        e = Entry("","\\U0001F354",10,3)
    with pytest.raises(ValueError):
        e = Entry("hamburger","",10,3)
    with pytest.raises(ValueError):
        e = Entry("hamburger","\\U0001F354",-1,3)
    with pytest.raises(ValueError):
        e = Entry("hamburger","\\U0001F354",10,-1)

def test_vendor():
    e1 = Entry("hamburger","\\U0001F354",10,2)
    e2 = Entry("pizza","\\U0001F355",8,1)
    e3 = Entry("salad","\\U0001F36D",6,1)
    v = Vendor([e1,e2,e3])
    assert len(v.get_available_entries_str()) == 3
    assert v.get_avaliable_free_indexes(2) == [3]
    assert v.get_avaliable_free_indexes(1) == [2,3]
    assert v.get_price_by_index(1) == 10
    assert v.get_price_by_index(2) == 4
    assert v.is_soldout == False
    v.sell(2)
    assert len(v.get_available_entries_str()) == 2
    assert v.sell(2) == False
    assert v.get_available_entries_indexes() == [1,3]
    with pytest.raises(ValueError):
        v = Vendor([])
    
def test_wallet():
    w = Wallet(10)
    assert w.balance == 10
    assert str(w) == "$10.00"
    w.spend(8)
    assert w.balance == 2
    assert str(w) == "$2.00"
    with pytest.raises(ValueError):
        w.spend(5)
    with pytest.raises(ValueError):
        w = Wallet(-5)


if __name__ == "__main__":
    main()
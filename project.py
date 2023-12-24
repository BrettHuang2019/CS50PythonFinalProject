import csv
from entry import Entry
from vendor import Vendor
from wallet import Wallet
import ui
import re

def main():
    start_balance = 50
    bought_items=[]

    user = get_user_name()
    ui.show_loading("Loading")
    ui.show_vendor_machine_title()
    vendor = init_vendor_machine()
    wallet = Wallet(start_balance)

    while not vendor.is_soldout and wallet.balance > vendor.get_cheapest_price():
        ui.show_vendor_machine(vendor.get_available_entries_str())
        ui.show_wallet_balance(user, str(wallet))
        ui.show_bought_items(bought_items, vendor)
        ui.show_select_promt()
        buy_one = get_buy_one(vendor, wallet)
        get_one = get_free_one(vendor.get_avaliable_free_indexes(buy_one))
        ui.show_loading("Purchasing")
        wallet.spend(vendor.get_price_by_index(buy_one))
        vendor.sell(buy_one)
        vendor.sell(get_one)
        bought_items.append(buy_one)
        bought_items.append(get_one)
        ui.show_purchase_success()
        ui.show_loading("Loading")

    ui.show_bought_items(bought_items, vendor)
    ui.show_end_game(start_balance - wallet.balance, vendor.is_soldout)


def init_vendor_machine():
    entrylist = []
    with open("inventory.csv","r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            entrylist.append(Entry(row["id"],row["emoji"],row["price"],row["amount"]))
    return Vendor(entrylist)


def get_user_name():
    while True:
        s = input("What's your name: ").strip()
        if name := validate_user_name(s):
            break
    return name

def validate_user_name(name):
    if m:= re.search(r"^(\w+)$", name):
        return m.group(1)
    return False

def get_buy_one(vendor, wallet):
    while True:
        i = get_index("Buy One: ", vendor.get_available_entries_indexes())
        if wallet.balance < vendor.get_price_by_index(i):
            print("😟Not enough balance to buy this item :(")
            continue
        elif i == 0:
            print("😟You cannot pick this number :(")
            continue
        else:
            break
    return i

def get_free_one(valid_indexes):
    if len(valid_indexes) >0:
        return get_index("Get One Free: ", valid_indexes)
    else: 
        return 0

def get_index(prompt, valid_indexes):
    while True:
        try:
            i = int(input(prompt).strip())
            if validate_index(i, valid_indexes):
                break
            else:
                print("😟You cannot pick this number :(")
                continue
        except ValueError:
            print("❌Please input a valid number")
    return i

def validate_index(i, valid_indexes):
    return  i in valid_indexes or i == 0

if __name__ == "__main__":
    main()
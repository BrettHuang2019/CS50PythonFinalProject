import csv
from entry import Entry
from vendor import Vendor
from wallet import Wallet
import ui

def main():
    start_balance = 50
    bought_items=[]

    user = ui.get_user_name()
    ui.show_vendor_machine_title()
    vendor = init_vendor_machine()
    wallet = Wallet(start_balance)

    while not vendor.is_soldout and wallet.balance > vendor.get_cheapest_price():
        ui.show_vendor_machine(vendor.get_available_entries_str())
        ui.show_wallet_balance(user, str(wallet))
        ui.show_bought_items(bought_items, vendor)
        ui.show_select_promt()
        buy_one = ui.get_buy_one(vendor, wallet)
        get_one = ui.get_free_one(vendor.get_avaliable_free_indexes(buy_one))
        wallet.spend(vendor.get_price_by_index(buy_one))
        vendor.sell(buy_one)
        vendor.sell(get_one)
        bought_items.append(buy_one)
        bought_items.append(get_one)
        ui.show_purchase_success()

    ui.show_bought_items(bought_items, vendor)
    ui.show_end_game(start_balance - wallet.balance, vendor.is_soldout)


def init_vendor_machine():
    entrylist = []
    with open("inventory.csv","r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            entrylist.append(Entry(row["id"],row["emoji"],row["price"],row["amount"]))
    return Vendor(entrylist)

if __name__ == "__main__":
    main()
from pyfiglet import Figlet
from tabulate import tabulate
import re
import cowsay
import time
import random

def show_vendor_machine_title():
    figlet = Figlet()
    figlet.setFont(font="drpepper")
    print(figlet.renderText("Welcome"))

def show_vendor_machine(entrylist):
    print( tabulate(entrylist, tablefmt="rounded_grid"))

def show_wallet_balance(name, balance):
    print( tabulate([[name+"'s wallet:", balance]], tablefmt="grid"))

def show_select_promt():
    print( "\n🛍️ Please choose your item.")

def show_purchase_success():
    print( "\n💰💰Purchase success!💰💰\n")

def show_bought_items(indexlist, vendor):
    if len(indexlist)>0:
        s = ""
        for i in indexlist:
            if i !=0:
                s = s+vendor.get_emoji_by_index(i)
        print("You have: "+s)

def show_loading(prompt):
    print(f"⏳⏳⏳{prompt}.",end="",flush=True)
    for _ in range(random.randint(3,5)):
        print(".",end="",flush=True)
        time.sleep(0.5)
    print("")
    

def show_end_game(spend, is_soldout):
    if is_soldout:
        line = "🎊Congratulations!🎊\nYou total spend is $"
    else: 
        line = "😢Too bad..You run out of money.😢\nTotal spend is $"
    cowsay.cow(line+str(spend))


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
            if i in valid_indexes or i == 0:
                break
            else:
                print("😟You cannot pick this number :(")
                continue
        except ValueError:
            print("ℹ️Please input a valid number")
    return i
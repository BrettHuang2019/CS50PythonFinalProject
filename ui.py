from pyfiglet import Figlet
from tabulate import tabulate
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
    for _ in range(random.randint(2,4)):
        print(".",end="",flush=True)
        time.sleep(0.5)
    print("")
    

def show_end_game(spend, is_soldout):
    if is_soldout:
        line = "🎊Congratulations!🎊\nYou total spend is $"
    else: 
        line = "😢Too bad..You run out of money.😢\nTotal spend is $"
    cowsay.cow(line+str(spend))


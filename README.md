# CS50's Vendor Machine
#### Video Demo:  https://youtu.be/UFulp3z9oP0

# Description: 
CS50's Vendor Machine is a console game where you use money to buy items. The goal is to buy all items while spending as little money as possible.

## Project Info

**Project:** CS50's Vendor Machine  
**Student:** Zhibin Huang  
**Location:** Montreal, Canada

## How to Play

1. Enter your name (without spaces).
2. See the welcome title, vendor machine items, and your wallet balance.
3. Choose an item to buy.
4. After buying, you'll see your owned items and go to the next round.
5. Win by buying all items or lose by running out of money.

## Purchase Rules:

1. Buy one, get one free. Input the index you want to buy and choose an item with LESS value for free. Enter 0 to skip the free item.
2. If no item qualifies for a free one, the purchase completes instantly.
3. The last item in each category is half price.
4. Buying a discounted item doesn't allow getting a full-price item for free, even if it's worth less.

#### Have fun playing the game! Try buying things in different orders and using different strategies to get the best deal!

## Third Party Pacakges

**PyFiglet**: This package is used for the game's welcome title.
**Tabulate**: Generate a grid view for the vending machine.
**Cowsay**: Display the end game screen indicating whether the user wins or loses at the end of the game.

## Project Structure
### inventory.csv 
This file serves as the data source for initializing the vending machine inventory in the main script(`project.py`). It contains information about different items, including their ID, emoji code, price, and initial quantity.

### projct.py 
The main script represents a simple text-based vending machine simulation. It reads input from the termianl and validate the input.

### wallet.py 
The `wallet.py` script defines a class called `Wallet`, representing a user's wallet in the vending machine simulation. It includes methods for initializing the wallet, retrieving the current balance, and spending money.

### entry.py 
The `entry.py` script defines a class called `Entry` that represents an entry in a vending machine inventory. Each entry has properties such as ID, emoji, price, and quantity.

### vendor.py 
The `vendor.py` script defines a class called `Vendor`, representing a vending machine. It includes methods to interact with the vending machine, such as selling items, retrieving information about available entries, and determining if the vending machine is sold out.

### ui.py 
The `ui.py` script provides a set of functions for displaying user interfaces and messages in the vending machine simulation. It utilizes external libraries such as `pyfiglet`, `tabulate`, `cowsay`, and the built-in `time` and `random` modules.

### test_project.py 
The `test_project.py` script contains a series of tests for the functions and classes defined in the project, including `validate_user_name`, `validate_index`, `init_vendor_machine`, `Entry`, `Vendor`, and `Wallet`.

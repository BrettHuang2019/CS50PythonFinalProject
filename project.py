import re
import csv

def main():
    get_user_name()
    init_vendor_machine()



def get_user_name():
    while True:
        s = input("Please enter your name (no spaces): ").strip()
        if name := validate_user_name(s):
            break
    return name

def validate_user_name(name):
    if m:= re.search(r"^(\w+)$", name):
        return m.group(1)
    return False


def init_vendor_machine():
    with open("inventory.csv","r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row["id"],row["emoji"],row["price"],row["amount"])


def function_n():
    ...


if __name__ == "__main__":
    main()
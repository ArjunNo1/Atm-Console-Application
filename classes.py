from collections import *

class ATM:
    def __init__(self) -> None:
        self.admins = defaultdict()
        self.users = defaultdict()

        # add denominations
        self.denominations = {2000:20, 500:20, 200:20, 100:20}
        self.balance  =  100*20 + 200*20 + 500*20 + 2000*20


class Admin:
    def __init__(self, name, pin) -> None:
        self.name = name
        self.pin = pin

    def __str__(self) -> str:
        return f"Name: {self.name}, Pin: {self.pin}"

    def __repr__(self) -> str:
        return f"Name: {self.name}, Pin: {self.pin}"



class User:
    def __init__(self, name, pin, balance) -> None:
        self.name = name
        self.pin = pin
        self.balance = balance
        self.transactions = []

    def __str__(self) -> str:
        return f"Name: {self.name}, Pin: {self.pin}, Balance: {self.balance}"

    def __repr__(self) -> str:
        return f"Name: {self.name}, Pin: {self.pin}, Balance: {self.balance}"

def handle_admin_command(cmd, atm):
    if cmd == "EXIT":
        return 0
            
    elif cmd == "HELP":
        print("Available commands are :")
        print("ADD USER")
        print("LOAD")
        print("BALANCE")
        print("EXIT")
        
    elif cmd == "ADD USER":
        name = input("Enter user name : ")
        pin = int(input("Enter user pin : "))
        balance = int(input("Enter user balance : "))
        user = User(name, pin, balance)
        atm.users[user.name] = user
        print(f"User {user.name} added successfully!")

    elif cmd == "LOAD":
        amount = atm.balance
        for denom in atm.denominations.keys():
            count = input(f"Enter number of {denom} notes : ")
            atm.denominations[denom] += int(count)
            atm.balance += int(count)*denom

            print(f"Total amount loaded is {atm.balance -amount}")
            
    elif cmd == "BALANCE":
        print(f"Total amount in ATM is {atm.balance}")
        print(f"Denominations are {atm.denominations.items()}")
                
def handle_user_command(cmd, atm, user):
    if cmd == "EXIT":
        return 0
    
    elif cmd == "HELP":
        print("Available commands are :")
        print("BALANCE")
        print("WITHDRAW")
        print("DEPOSIT")
        print("CHANGE PIN")
        print("EXIT")

    elif cmd == "BALANCE":
        print(f"Your balance is {user.balance}")
    elif cmd == "WITHDRAW":
        amount = int(input("Enter amount to withdraw : "))
        if amount > user.balance:
            print("Insufficient user balance!")
        elif amount > atm.balance:
            print("Insufficient balance in ATM!")
        else:
            temp_user_balance = user.balance
            temp_atm_denominations = atm.denominations.copy()
            temp_atm_balance = atm.balance

            for denom in atm.denominations.keys():
                count = amount//denom
                if count > atm.denominations[denom]:
                    continue
                temp_atm_denominations[denom] -= count
                temp_atm_balance -= count*denom
                temp_user_balance -= count*denom
                amount -= count*denom
            
            if amount != 0:
                print("Unable to withdraw amount!")
            else:
                collected_cash = defaultdict(lambda:0)
                
                for denominations in temp_atm_denominations.keys():
                    collected_cash[denominations] = atm.denominations[denominations] - temp_atm_denominations[denominations]

                print("Cash format : ",collected_cash.items())
                print(f"Please collect your cash {user.balance-temp_user_balance}. Your current balance is {temp_user_balance}")
                user.transactions.append(f"Withdrawal of {user.balance-temp_user_balance}")
                atm.denominations = temp_atm_denominations
                atm.balance = temp_atm_balance
                user.balance = temp_user_balance
                


            


    elif cmd == "DEPOSIT":
                # deposit with denominations
        amount = int(input("Enter amount to deposit : "))
        prev_balance = user.balance
        for denom in atm.denominations.keys():
            count = input(f"Enter number of {denom} notes : ")
            atm.denominations[denom] += int(count)
            atm.balance += int(count)*denom
            user.balance += int(count)*denom
                
        print(f"Your current balance is {user.balance}")

        user.transactions.append(f"Deposit of {user.balance-prev_balance}")

    elif cmd == "CHANGE PIN":
        new_pin = input("Enter new pin : ")
        user.pin = new_pin
        print("Pin changed successfully!")
        user.transactions.append(f"Pin changed to {new_pin}")
            
    elif cmd == "TRANSFER":
        to_user = input("Enter user name to transfer : ")
        if to_user not in atm.users.keys():
            print("User not found!")
        else:
            amount = int(input("Enter amount to transfer : "))
            if amount > user.balance:
                print("Insufficient balance!")
            else:
                user.balance -= amount
                atm.users[to_user].balance += amount
                print(f"Amount transferred successfully! Your current balance is {user.balance}")
                user.transactions.append(f"Transfer of {amount} to {to_user}")
                atm.users[to_user].transactions.append(f"Transfer of {amount} from {user.name}")
            
    elif cmd == "TRANSACTIONS":
        print(user.transactions)
    




def get_int(message):
    num = input(message)
    try:
        num = int(num)
    except ValueError:
        print("Please, use numbers only!\n")
        get_int(message)
    else:
        return num

def get_acc(database):
    while True:
        acc = get_int("\nPlease enter your account number: ")
        acc_nums = []
        for i in range(len(database)): 
            acc_nums += [database[i][0]]
        if acc in acc_nums:
            return acc
        else:
            print("Account doesn't exist!")

def find_userid(database, acc):
    for i in range(len(database)):
        if acc == database[i][0]:
            return i

def get_pin(database, userid):
    while True:
        pin = get_int("\nEnter your PIN: ")
        if pin != database[userid][1]:
            print('Wrong PIN')
            continue
        return pin

def authenticate(acc, pin, database, userid):
    for i in range(len(database)):
        if acc == database[userid][0] and pin == database[userid][1]:
            return True
        else:
            return False

def withdraw(database, atmcash, userid):
    while True:
        print("\nWithdrawal Menu")
        print("   1 - $20     4 - $100")
        print("   2 - $40     5 - $200")
        print("   3 - $60     6 - Cancel transaction")
        choice = get_int("Choose a withdrawal amount: ")
        common = [20, 30, 60, 100, 200]
        if choice in range(6):
            amount = common[choice - 1]
        elif choice == 6:
            print("Transaction Cancelled ")
            amount = "continue"
        else:
            print("invalid input")
            continue
        
        if amount <= database[userid][2]:
            pass
        else: 
            print("You don't have enough balance")
            break
        if amount <= atmcash:
            pass
        else: 
            print("The ATM doesn't have enough cash")
            break
        return amount

def balance(userid):
    print(f"\nYour balance is ${database[userid][2]}")

def deposit():
    amount = get_int("\nEnter a deposit amount or type 0 to cancel: ")
    if amount == 0:
        amount = "break"
    else:
        print("\nPlease insert a deposit envelope within two minutes")
        envelope = True
        if envelope == True:
            print("\nDeposit envelope succesfully recieved")
            print("Your account will be updated as soon as your envelop reaches authorities")
        else:
            print("The system has canceled the transaction due to inactivity")
            amount = "break"
    return amount

def exit():
    print("\nThanks for your time!")
    return "break"


while True:
    print("\nWelcome")
    database = [
        [12345, 54321, 1200],
        [47531, 13574, 2000],
        ]
    atmcash = 1000
    acc = get_acc(database)
    userid = find_userid(database, acc)
    pin = get_pin(database, userid)

    while True:
        print("\nMain menu")
        print("  1 - View my balance")
        print("  2 - Withdraw cash")
        print("  3 - Deposit funds")
        print("  4 - Exit")
        choice = get_int("Enter your choice: ")

        if choice == 1:
            balance(userid)
        elif choice == 2:
            amount = withdraw(database, atmcash, userid)
            if amount != "continue":
                atmcash -= amount
                database[userid][2] -= amount
                print("\nYou have successfully taken out your money")
                print(f"Your account balance is ${database[userid][2]}\n")
            else:
                continue
        elif choice == 3:
            amount = deposit()
            if amount == "continue":
                continue
        elif choice == 4:
            exit("Thanks for your time!")
        else:
            print('Please, pick from the choices shown below!')

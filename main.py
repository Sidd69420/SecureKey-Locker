from pwinput import pwinput
from config import setting_masterpass, check_db

try:
    while True:
        import scripts
        break
except:
    check_db()
    import scripts


def mpass_input():
    with open("mpass.txt", "r") as pass_store:
        actual_password = pass_store.read()

    if actual_password =="":
        print("You have no master password set. Let's setup the password manager first!")
        setting_masterpass()
    else:
        print("Hello! Before we proceed, confirm your identity!\n")
        master_pass_input = pwinput(prompt="Enter Master Password: ", mask="*")

        if master_pass_input == actual_password:
            Main_menu()
        else:
            print("The entered Master Password is wrong! Try again...")

def master_password_changer():
    new_pass = pwinput(prompt="Please enter the new Master Password: ", mask="*")
    confirm = pwinput(prompt="Please confirm the password: ", mask="*")

    if new_pass == confirm:
        with open('mpass.txt', "w") as f:
            f.write(new_pass)
        print("Your master password has been changed\n")
    else:
        print("The password don't match... Please try again!")

def Main_menu():
    print("Amigo! Welcome to SecureKey Locker!")

    while True:
        print("\nEnter the corresponding numbers to select- \n1. Add\n2. Remove\n3. Update\n4. View\n5. Random Password Generator\n6. Master Password Changer\n7. Exit")
        Choice= input("Enter your choice: ")
        if Choice == "1": scripts.add_pass()
        elif Choice == "2": scripts.rem_pass()
        elif Choice == "3": scripts.update_pass()
        elif Choice == "4": scripts.view_db()
        elif Choice == "5": scripts.rand_passgen()
        elif Choice == "6": master_password_changer()
        elif Choice == "7" or Choice == "exit": break
        else: print("Not a valid choice... Try again!\n")

mpass_input()

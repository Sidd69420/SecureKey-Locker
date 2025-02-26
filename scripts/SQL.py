import mysql.connector as sqlcon
from pwinput import pwinput
from scripts.tables import table_creator
from os import environ
from pyperclip import copy

passwd1 = environ.get("PASSWORD")


SecureKey_Locker = sqlcon.connect(host = "localhost",
                                  user = "root",
                                  passwd = passwd1,
                                  database = "SecureKey_Locker")

PM_cur = SecureKey_Locker.cursor()

def add_pass():
  website = input("Enter website name: ")
  username = input("Enter your username: ")

  password = pwinput(prompt="Enter your password: ", mask="*")
  confirm_pass = pwinput(prompt="Enter your password once more to confirm: ", mask="*")

  while password != confirm_pass:
    print("Passwords didn't match. Try again.")
    password = pwinput(prompt="Enter your password: ", mask="*")
    confirm_pass = pwinput(prompt="Enter your password once more to confirm: ", mask="*")

  print("Passwords matched.")
  PM_cur = SecureKey_Locker.cursor()
  insert_str = f"INSERT INTO Pass(Website, Username, Password) VALUES('{website}', '{username}','{confirm_pass}');"
  PM_cur.execute(insert_str)
  SecureKey_Locker.commit()

  print("Entry added to database!")

def rem_pass():
    website = input("Enter the website from which you want to remove the password entry: ")
    search_str = f"SELECT * FROM Pass WHERE Website='{website}'"
    PM_cur = SecureKey_Locker.cursor()
    PM_cur.execute(search_str)
    result = PM_cur.fetchall()
    table_creator(result)
    entry_no = int(input("Which S No. of record you want to delete?"))
    rem_str = f"DELETE FROM Pass WHERE Username=\"{result[entry_no - 1][1]}\""
    PM_cur = SecureKey_Locker.cursor()
    PM_cur.execute(rem_str)
    SecureKey_Locker.commit()

    print("Password sucessfully deleted.")

def update_pass():
    disp_str = "SELECT * FROM Pass"
    PM_cur.execute(disp_str)
    result = PM_cur.fetchall()
    table_creator(result)
    entry_no = int(input("Which S No. of record you want to update? "))
    website = input("Enter website name: ")
    username = input("Enter username: ")
    password = pwinput(prompt="Enter new password: ", mask="*")
    update_str = f"UPDATE Pass SET Website='{website}', Username='{username}', Password='{password}' WHERE Website='{result[entry_no - 1][0]}'AND Username='{result[entry_no-1][1]}'"
    PM_cur.execute(update_str)
    SecureKey_Locker.commit()

    print("Record successfully updated!")

def view_db():
  choice=input(" 1. View all enteries of the database \n 2. To view passwords of a specific website\n Enter your choice: ")
  if choice=="1":
    def view_all_db():
      disp_str = "SELECT * FROM Pass"
      PM_cur.execute(disp_str)
      result = PM_cur.fetchall()
      table_creator(result)
      clipboard_confirm = input("Would you like to copy password to clipboard? ")
      if clipboard_confirm == "Yes" or clipboard_confirm == "y" or clipboard_confirm == "yes":
        entry_no = int(input("Which S No. of record you want to copy? "))
        copy(result[entry_no - 1][2])
        print("Password copied successfully!\n")
      else:
        print("Nothing was copied to clipboard.\n")

    view_all_db()
  if choice == "2":
    def View_website():
      website = input("Enter the website which you want to search: ")
      search_str = f"SELECT * FROM Pass WHERE Website='{website}'"
      PM_cur = SecureKey_Locker.cursor()
      PM_cur.execute(search_str)
      result = PM_cur.fetchall()
      table_creator(result)
      clipboard_confirm = input("Would you like to copy password to clipboard? ")
      if clipboard_confirm == "Yes" or clipboard_confirm == "y" or clipboard_confirm == "yes":
        entry_no = int(input("Which S No. of record you want to copy? "))
        copy(result[entry_no - 1][2])
        print("Password copied successfully!\n")
      else:
        print("Nothing was copied to clipboard.\n")

    View_website()

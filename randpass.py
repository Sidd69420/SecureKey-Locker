import random
from pyperclip import copy

def rand_passgen():
  pswd = ''
  pool = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890')

  passwd_length = int(input("Enter no of characters you want in your password(at most 25): "))

  for i in range(passwd_length):
    num = random.randint(0,len(pool)-1)
    digit = str(pool[num])
    pswd += digit

  print ('Your random password is ', pswd)
  clip_confirm = input("Would you like to copy this password to clipboard? ")

  if clip_confirm == "yes" or clip_confirm == "Yes" or clip_confirm == "y":
    copy(pswd)
    print("Your password was copied to the clipboard!")
  else:
    print("Nothing was copied to clipboard.")

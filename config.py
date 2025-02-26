import mysql.connector as sqlcon
from pwinput import pwinput 
from os import environ

passwd1 = environ.get("PASSWORD")

SecureKey_Locker = sqlcon.connect(host = "localhost",
                                 user = "root",
                                 passwd = passwd1)

PM_cur = SecureKey_Locker.cursor()

def setting_masterpass():
    while True:
        new_master_password = pwinput(prompt="Enter your new master-password: ", mask="*")
        confirm = pwinput(prompt="Re-enter your new master-password: ", mask="*")
    
        if new_master_password == confirm:
            with open("mpass.txt", "w") as file:
                file.write(confirm)
            break
        else: 
            print("Passwords don't match... Try again!")
            
def check_db():
    PM_cur.execute("SHOW DATABASES LIKE 'SecureKey_Locker'")
    results = PM_cur.fetchall()
    
    if results:
        print("Cool you already have the database!")
        return True
    else:
        print("No existing database found. We will now create it!")
        db_str = "CREATE DATABASE SecureKey_Locker"
        table_str = "CREATE TABLE Pass(Website varchar(15), Username varchar(35), Password varchar(80))"
        PM_cur.execute(db_str)
        PM_cur.execute("USE SecureKey_Locker")
        PM_cur.execute(table_str)
        SecureKey_Locker.commit()
        print("Database and table created!")
        
        return False
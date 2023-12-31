import tkinter as tk
from tkinter import messagebox

import mysql.connector
import configparser

# Read MySQL config file
config = configparser.ConfigParser()
config.read('config.ini')

db_host = config['mysql']['host']
db_user = config['mysql']['user']
db_password = config['mysql']['password']
db_name = config['mysql']['database']

class RegisterWindow(tk.Frame):
    def __init__(self, root, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = root
        self.parent = parent
        #Welcome label
        tk.Label(self.parent, 
                 text="Register Menu", 
                 font=("Arial", 40)).grid(row = 0, column=0, pady=5)
        #instructions label
        tk.Label(self.parent, 
                 text="Please fill out the information below to create an account.", 
                 font=("Arial", 10)).grid(row = 1, column=0, pady=5)
        
        #Username label
        tk.Label(self.parent, 
                 text="Username", 
                 font=("Arial", 10)).grid(row = 2, column=0, sticky = "W", pady=5)
        #Password label
        tk.Label(self.parent, 
                 text="Password", 
                 font=("Arial", 10)).grid(row = 3, column=0, sticky = "W", pady=5)
        
        #username entry
        username = tk.Entry(self.parent)
        username.grid(row=2,column=0,pady=5)
        password = tk.Entry(self.parent,  show="*")
        password.grid(row=3,column=0,pady=5)

        #register button
        tk.Button(self.parent,
                  text="Register",
                  width=25,
                  command= lambda: self.RegisterAccount(username.get(), password.get()),
                  ).grid(row = 4, column=0, pady=2)
        #back button
        tk.Button(self.parent,
                  text="Back to main menu",
                  width=25,
                  command= self.OpenMainMenu,
                  ).grid(row = 5, column=0, pady=2)
        
    def RegisterAccount(self, username, pw):
        if username == "" or pw == "":
            messagebox.showwarning("Failed to register!", "You need to fill out the fields to register.")
        else:
            try:
                connection = mysql.connector.connect(
                    host=db_host,
                    user=db_user,
                    password=db_password,
                    database=db_name
                )
                cursor = connection.cursor()

                check_entries = "SELECT * FROM registered WHERE username = %s"
                username_to_check = (username,)
                cursor.execute(check_entries, username_to_check)
                result = cursor.fetchone()

                if result:
                    messagebox.showerror("Failed to register!", "The username you entered is already taken.")
                else:
                    insert_account = "INSERT INTO registered (username, pw) VALUES (%s, %s)"
                    account_info = (username, pw)
                    cursor.execute(insert_account, account_info)
                    connection.commit()
                    messagebox.showinfo("'Successfully registered'!", "You have registered a new account!")
            except mysql.connector.Error as err:
                print(f"Error: {err}")
            finally:
                if connection:
                    connection.close()

    def OpenMainMenu(self):
        self.root.deiconify()
        self.parent.destroy()
import tkinter as tk
from tkinter import messagebox
import sqlite3

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
                  command=self.RegisterAccount(lambda: username.get(), password.get()),
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
            registered_accounts_db = sqlite3.connect('registered_accounts.db')
            db_cursor = registered_accounts_db.cursor()

            db_cursor.execute("""SELECT username FROM registered WHERE username=?""",(username))

            result = db_cursor.fetchone()
            if result:
                messagebox.showwarning("Failed to register!", "The username you entered is already taken.")
            else:
                db_cursor.execute("INSERT INTO registered VALUES (:username, :pw,)",
                                {
                                    'username': username,
                                    'password': pw
                                })
                registered_accounts_db.commit()
                registered_accounts_db.close()
        
    def OpenMainMenu(self):
        self.root.deiconify()
        self.parent.destroy()
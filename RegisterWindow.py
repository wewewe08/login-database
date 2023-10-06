import tkinter as tk

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
        username = tk.Entry(self.parent).grid(row=2,column=0,pady=5)
        password = tk.Entry(self.parent,  show="*").grid(row=3,column=0,pady=5)

        #login button
        tk.Button(self.parent,
                  text="Register",
                  width=25,
                  #command=,
                  ).grid(row = 4, column=0, pady=2)
        #back button
        tk.Button(self.parent,
                  text="Back to main menu",
                  width=25,
                  command= self.OpenMainMenu,
                  ).grid(row = 5, column=0, pady=2)
        
    def OpenMainMenu(self):
        self.root.deiconify()
        self.parent.destroy()
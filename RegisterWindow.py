import tkinter as tk

class RegisterWindow(tk.Frame):
    def __init__(self, root, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = root
        self.parent = parent
        #Welcome label
        tk.Label(self.parent, 
                 text="Register Menu", 
                 font=("Arial", 40),
                 pady=10).pack()
        #instructions label
        tk.Label(self.parent, 
                 text="Please fill out the information below to create an account.", 
                 font=("Arial", 10),
                 pady=10).pack()
        #login button
        tk.Button(self.parent,
                  text="Register",
                  width=25,
                  #command=,
                  ).pack(pady=5)
        #back button
        tk.Button(self.parent,
                  text="Back to main menu",
                  width=25,
                  command= self.OpenMainMenu,
                  ).pack(pady=5)
        
    def OpenMainMenu(self):
        self.root.deiconify()
        self.parent.destroy()
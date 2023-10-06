import tkinter as tk

from LoginWindow import LoginWindow
from RegisterWindow import RegisterWindow

class MainWindow(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        #Welcome label
        tk.Label(self.parent, 
                 text="Main Menu", 
                 font=("Arial", 40),
                 pady=10).pack()
        #instructions label
        tk.Label(self.parent, 
                 text="Please select an option below.", 
                 font=("Arial", 10),
                 pady=20).pack()
        #login button
        tk.Button(self.parent,
                  text="Login",
                  width=25,
                  command=self.OpenLoginScreen
                  ).pack(pady=5)
        #register button
        tk.Button(self.parent,
                  text="Register",
                  width=25,
                  command=self.OpenRegisterScreen
                  ).pack(pady=5)
        
    def OpenLoginScreen(self):
        self.OpenLoginScreen = tk.Toplevel(self.parent)
        self.parent.eval(f"tk::PlaceWindow {str(self.OpenLoginScreen)} center")
        self.app = LoginWindow(self.parent, self.OpenLoginScreen)
        self.parent.withdraw()

    def OpenRegisterScreen(self):
        self.OpenRegisterScreen = tk.Toplevel(self.parent)
        self.parent.eval(f"tk::PlaceWindow {str(self.OpenRegisterScreen)} center")
        self.app = RegisterWindow(self.parent, self.OpenRegisterScreen)
        self.parent.withdraw()
import tkinter as tk

from MainWindow import MainWindow

class MainApp(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.main_window = MainWindow(self.parent)

        self.main_window.pack(side="top", fill="both")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("login-database")
    root.eval("tk::PlaceWindow . center") #centers window

    app = MainApp(root)
    root.mainloop()
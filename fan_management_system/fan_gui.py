import tkinter as tk
from tkinter import Frame, Label
from testfan import TestFan

class FanGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("💨 Fan Management System")
        self.root.geometry("850x500")
        self.root.configure(bg="#121212")

        # Resizable window
        self.root.resizable(True, True)

        # Minimum size
        self.root.minsize(700, 400)

        self.test_fan = TestFan()
        self.fan1, self.fan2 = self.test_fan.get_fans()

        self.create_ui()

        self.root.mainloop()
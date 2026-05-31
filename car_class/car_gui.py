import tkinter as tk
from tkinter import ttk
from car import Car

class CarGUI:
    def __init__(self):

        self.car = Car(2025, "Ferrari 296 GTS")

        self.root = tk.Tk()
        self.root.title("Ferrari GTS Speed Simulator")

        self.root.geometry("1000x650")
        self.root.minsize(900, 600)

        self.root.configure(bg="#0f0f0f")

        self.setup_ui()

        self.root.mainloop()
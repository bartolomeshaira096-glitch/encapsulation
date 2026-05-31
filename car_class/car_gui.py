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

    def setup_ui(self):

        title = tk.Label(
            self.root,
            text="FERRARI 296 GTS",
            font=("Montserrat", 34, "bold"),
            bg="#0f0f0f",
            fg="#ff2e2e"
        )
        title.pack(pady=20)

        subtitle = tk.Label(
            self.root,
            text="Luxury Performance Speed Simulator",
            font=("Segoe UI", 14),
            bg="#0f0f0f",
            fg="white"
        )
        subtitle.pack()

        info = tk.Label(
            self.root,
            text=f"Year Model: {self.car.get_year_model()}",
            font=("Segoe UI", 14),
            bg="#0f0f0f",
            fg="#cccccc"
        )
        info.pack(pady=10)
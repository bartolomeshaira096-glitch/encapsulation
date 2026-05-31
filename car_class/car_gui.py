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

        self.speed_label = tk.Label(
            self.root,
            text="0 KM/H",
            font=("Impact", 60),
            bg="#0f0f0f",
            fg="#00ff99"
        )
        self.speed_label.pack(pady=50)

        button_frame = tk.Frame(
            self.root,
            bg="#0f0f0f"
        )
        button_frame.pack()

        accelerate_btn = tk.Button(
            button_frame,
            text="ACCELERATE",
            font=("Segoe UI", 16, "bold"),
            bg="#ff2e2e",
            fg="white",
            width=15,
            height=2,
            relief="flat",
            command=self.accelerate
        )
        accelerate_btn.grid(row=0, column=0, padx=15)

        brake_btn = tk.Button(
            button_frame,
            text="BRAKE",
            font=("Segoe UI", 16, "bold"),
            bg="#444444",
            fg="white",
            width=15,
            height=2,
            relief="flat",
            command=self.brake
        )
        brake_btn.grid(row=0, column=1, padx=15)
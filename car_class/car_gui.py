import tkinter as tk
from tkinter import ttk
from car import Car
from PIL import Image, ImageTk

class CarGUI:
    def __init__(self):

        self.car = Car(2025, "Ferrari 296 GTS")

        self.root = tk.Tk()
        self.root.title("Ferrari GTS Speed Simulator")

        self.root.geometry("1000x650")
        self.root.minsize(900, 600)

        self.original_bg = Image.open("car_class/ferrari_bg.jpg")

        self.bg_label = tk.Label(self.root)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.root.bind("<Configure>", self.resize_bg)

        self.setup_ui()

        self.root.mainloop()

    def resize_bg(self, event=None):

        width = self.root.winfo_width()
        height = self.root.winfo_height()

        resized = self.original_bg.resize(
            (width, height),
            Image.Resampling.LANCZOS
        )

        self.bg_photo = ImageTk.PhotoImage(resized)

        self.bg_label.config(image=self.bg_photo)

    def setup_ui(self):

        title = tk.Label(
            self.root,
            text="FERRARI 296 GTS",
            font=("Montserrat", 34, "bold"),
            bg="black",
            fg="#ff2e2e"
        )
        title.pack(pady=20)
        title.lift()

        subtitle = tk.Label(
            self.root,
            text="Luxury Performance Speed Simulator",
            font=("Segoe UI", 14),
            bg="black",
            fg="white"
        )
        subtitle.pack()
        subtitle.lift()

        info = tk.Label(
            self.root,
            text=f"Year Model: {self.car.get_year_model()}",
            font=("Segoe UI", 14),
            bg="black",
            fg="#cccccc"
        )
        info.pack(pady=10)
        info.lift()

        self.speed_label = tk.Label(
            self.root,
            text="0 KM/H",
            font=("Impact", 60),
            bg="black",
            fg="#00ff99"
        )
        self.speed_label.pack(pady=50)
        self.speed_label.lift()

        button_frame = tk.Frame(
            self.root,
            bg="black"
        )
        button_frame.pack()
        button_frame.lift()

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

        demo_btn = tk.Button(
            self.root,
            text="RUN ACTIVITY DEMO",
            font=("Segoe UI", 15, "bold"),
            bg="#00aa66",
            fg="white",
            relief="flat",
            command=self.run_demo
        )
        demo_btn.pack(pady=40)

        self.log = tk.Text(
            self.root,
            height=10,
            width=70,
            bg="#181818",
            fg="white",
            font=("Consolas", 12)
        )
        self.log.pack(pady=10)

    def update_speed(self):
        speed = self.car.get_speed()

        self.speed_label.config(
            text=f"{speed} KM/H"
        )

    def accelerate(self):
        self.car.accelerate()

        self.update_speed()

        self.log.insert(
            tk.END,
            f"Accelerate -> Speed: {self.car.get_speed()} km/h\n"
        )

        self.log.see(tk.END)

    def brake(self):
        self.car.brake()

        self.update_speed()

        self.log.insert(
            tk.END,
            f"Brake -> Speed: {self.car.get_speed()} km/h\n"
        )

        self.log.see(tk.END)

    def run_demo(self):

        self.log.delete(1.0, tk.END)

        self.log.insert(
            tk.END,
            "===== ACTIVITY OUTPUT =====\n\n"
        )

        for _ in range(5):
            self.car.accelerate()

            self.log.insert(
                tk.END,
                f"Accelerate -> {self.car.get_speed()} km/h\n"
            )

        self.log.insert(
            tk.END,
            "\n"
        )

        for _ in range(5):
            self.car.brake()

            self.log.insert(
                tk.END,
                f"Brake -> {self.car.get_speed()} km/h\n"
            )

        self.update_speed()
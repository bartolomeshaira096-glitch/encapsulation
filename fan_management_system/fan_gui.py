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

     def create_ui(self):
        title = Label(
            self.root,
            text="💨 FAN MANAGEMENT SYSTEM",
            font=("Segoe UI", 24, "bold"),
            bg="#121212",
            fg="white"
        )
        title.pack(pady=20)

        container = Frame(self.root, bg="#121212")
        container.pack(expand=True, fill="both", padx=20)

        self.create_fan_card(
            container,
            self.fan1,
            "🔥 Fan 1",
            "#FFD54F"
        ).pack(side="left", expand=True, fill="both", padx=15)

        self.create_fan_card(
            container,
            self.fan2,
            "🌬️ Fan 2",
            "#64B5F6"
        ).pack(side="right", expand=True, fill="both", padx=15)
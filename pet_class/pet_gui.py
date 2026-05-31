import tkinter as tk
from pet import Pet
from tkinter import messagebox

class PetGUI:
    def __init__(self):
        self.pet = Pet()

        self.window = tk.Tk()
        self.window.title("🐾 Pet Information System")
        self.window.geometry("600x400")
        self.window.resizable(True, True)

        self.bg_image = tk.PhotoImage(file="pet_bg.png")
        self.bg_label = tk.Label(self.window, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)

        self.frame = tk.Frame(self.window, bg="#000000", bd=0)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
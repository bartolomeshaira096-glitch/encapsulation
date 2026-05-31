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
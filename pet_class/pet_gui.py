import tkinter as tk
from pet import Pet
from tkinter import messagebox
from PIL import Image, ImageTk

class PetGUI:
    def __init__(self):
        self.pet = Pet()

        self.window = tk.Tk()
        self.window.title("🐾 Pet Information System")
        self.window.geometry("600x400")
        self.window.resizable(True, True)

        img_path = "pet_class/pet_bg.png"

        image = Image.open(img_path)
        self.bg_image = ImageTk.PhotoImage(image)
        self.bg_label = tk.Label(self.window, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)

        self.frame = tk.Frame(self.window, bg="#000000", bd=0)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(
            self.frame,
            text="PET INFO SYSTEM",
            font=("Helvetica", 18, "bold"),
            fg="white",
            bg="black"
        ).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.frame, text="Name:", fg="white", bg="black").grid(row=1, column=0)
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.grid(row=1, column=1)

        tk.Label(self.frame, text="Type:", fg="white", bg="black").grid(row=2, column=0)
        self.type_entry = tk.Entry(self.frame)
        self.type_entry.grid(row=2, column=1)

        tk.Label(self.frame, text="Age:", fg="white", bg="black").grid(row=3, column=0)
        self.age_entry = tk.Entry(self.frame)
        self.age_entry.grid(row=3, column=1)

        tk.Button(
            self.frame,
            text="SAVE PET",
            command=self.save_pet,
            bg="red",
            fg="white"
        ).grid(row=4, column=0, columnspan=2, pady=10)

        self.output = tk.Label(self.frame, text="", fg="white", bg="black")
        self.output.grid(row=5, column=0, columnspan=2)

        self.window.mainloop()

    def save_pet(self):
        name = self.name_entry.get()
        animal_type = self.type_entry.get()
        age = self.age_entry.get()

        if name == "" or animal_type == "" or age == "":
            messagebox.showerror("Error", "Complete all fields!")
            return
        
        self.pet.set_name(name)
        self.pet.set_animal_type(animal_type)
        self.pet.set_age(age)

        result = f"🐶 Name: {self.pet.get_name()}\n🐱 Type: {self.pet.get_animal_type()}\n🎂 Age: {self.pet.get_age()}"
        self.output.config(text=result)
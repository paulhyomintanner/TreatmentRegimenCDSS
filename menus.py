import customtkinter as ctk
from tkinter import Canvas, Scrollbar
import json

class AppModel:
    def __init__(self):
        self.data = self.load_data()
        self.rejected_treatments = []
        self.user_data = {
        "weight": None,
        "height": None,
        "age": None, 
        "cpg": None,
        "diseases": [],
        "exclusions": []
    }
    def reset_data(self):
        self.user_data = {
            "weight": None,
            "height": None,
            "age": None, 
            "cpg": None,
            "diseases": [],
            "exclusions": []
        }
        self.rejected_treatments = []
    def load_data(self):
        with open('dosing_db.json') as f:
            data = json.load(f)
        return data


class AppView(ctk.CTkScrollableFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # Initialize view components here
        self.label = ctk.CTkLabel(self, text="")
        self.label.grid(row=0, column=0, padx=20, pady=20)

    def update_data(self, data):
        self.label.configure(text=data)

class AppController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.initialize_ui()

    def initialize_ui(self):
        data = self.model.get_data()
        self.view.update_data(data)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("TreatmentCDSS")
        
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("dark-blue")
        
        self.geometry("500x800")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.model = AppModel()
        self.view = AppView(self, width=500, height=800, corner_radius=0, fg_color="transparent")
        self.view.grid(row=0, column=0, sticky="nsew")
        self.controller = AppController(self.model, self.view)

if __name__ == "__main__":
    app = App()
    app.mainloop()

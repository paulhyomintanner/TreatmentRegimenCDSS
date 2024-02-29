import customtkinter as ctk
import tkinter as tk
import json
ctk.set_appearance_mode("Dark")  
ctk.set_default_color_theme("dark-blue")  

class Data:
    def __init__(self):
        self.data = self.load_data()
    def load_data(self):
        with open('dosing_db.json') as f:
            data = json.load(f)
        return data


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        data_instance = Data()
        self.data = data_instance.data
        cpgs = list(set(cpg for treatment in self.data['_default'].values() for cpg in treatment['rank'][0]))
        exclusions = list(set(exclusion for treatment in self.data['_default'].values() for eligibility in treatment['eligibility'] for exclusion in eligibility['exclusion']))
        diseases = list(set(treatment['disease'] for treatment in self.data['_default'].values()))

        self.geometry("1000x700")
        self.title("small example app")
        self.minsize(300, 200) 

        # create 2x2 grid system
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14), weight=1)
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)

        #inputs for the UI
        self.cpg_dropdown = ctk.CTkOptionMenu(master=self, values=cpgs, width=10)
        self.cpg_dropdown.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.height_entry = ctk.CTkEntry(master=self, placeholder_text="Height")
        self.height_entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.weight_entry = ctk.CTkEntry(master=self, placeholder_text="Weight")
        self.weight_entry.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.exclusions = ctk.CTkLabel(master=self, text="Select exclusions that apply:")
        self.exclusions.grid(row=3, column=0, padx=10, pady=5)

        self.exclusion_checkboxes = {}  
        for i, exclusion in enumerate(exclusions):
            cb = ctk.CTkCheckBox(master=self, text=exclusion)
            cb.grid(row=4 + i, column=0, sticky="nsew")
            self.exclusion_checkboxes[exclusion] = cb

        self.diseases = ctk.CTkLabel(master=self, text="Select disease:")
        self.disease_dropdown = ctk.CTkOptionMenu(master=self, values=diseases)
        self.disease_dropdown.grid(row=10, column=0, padx=10, pady=5)

        self.display_textbox = ctk.CTkTextbox(master=self)
        self.display_textbox.grid(row=0, column=1,columnspan=3, rowspan=14, padx=10, pady=10, sticky="nsew")

        self.button = ctk.CTkButton(master=self, command=self.button_callback, text="Confirm Selection")
        self.button.grid(row=13, column=0, padx=10, pady=10, sticky="ew")


    def button_callback(self):
        self.display_textbox.insert("end", self.combobox.get() + "\n")

    def get_exclusions(self):
        selected_exclusions = []
        for exclusion, checkbox in self.exclusion_checkboxes.items():
            if checkbox.value.get():
                selected_exclusions.append(exclusion)
        return selected_exclusions

if __name__ == "__main__":
    app = App()
    app.mainloop()
import customtkinter as ctk
import tkinter as tk
import json

# Set appearance and color theme
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

class Data:
    def __init__(self):
        self.data = self.load_data()
        self.rules = self.load_superseding_rules()
        
    def load_data(self):
        # Ensure the filename matches the file's actual location and name
        with open('menuTinyDB.json') as f:
            data = json.load(f)
        return data
    
    def load_superseding_rules(self):
        with open('superseding_rules_db.json') as f:
            rules = json.load(f)
        return rules["_default"]

    def map_disease_to_severity(self):
        disease_to_severity = {}
        for treatment in self.data['_default'].values():
            disease = treatment['disease']
            severities = set()
            for eligibility in treatment['eligibility']:
                for severity_type, severity_value in eligibility['severity'].items():
                    severities.add(f"{severity_type}: {severity_value}")
            if disease in disease_to_severity:
                disease_to_severity[disease].update(severities)
            else:
                disease_to_severity[disease] = severities
        return {disease: sorted(severities) for disease, severities in disease_to_severity.items()}
    

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        data_instance = Data()
        self.data = data_instance.data
        self.disease_to_severity = data_instance.map_disease_to_severity()
        
        self.user_data = {
        "weight": None,
        "height": None,
        "age": None, 
        "cpg": None,
        "diseases": [],
        "exclusions": []
    }

        self.geometry("1000x700")
        self.title("Small Example App")
        self.minsize(300, 200)

        # create 2x2 grid system
        self.grid_rowconfigure(list(range(15)), weight=1)
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)

        # Inputs for the UI
        cpgs = list(set(cpg for treatment in self.data['_default'].values() for cpg in treatment['rank'][0]))
        self.cpg_dropdown = ctk.CTkOptionMenu(master=self, values=cpgs, width=10)
        self.cpg_dropdown.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.height_entry = ctk.CTkEntry(master=self, placeholder_text="Height")
        self.height_entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.weight_entry = ctk.CTkEntry(master=self, placeholder_text="Weight")
        self.weight_entry.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.age_entry = ctk.CTkEntry(master=self, placeholder_text="Age")
        self.age_entry.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
        
        exclusions = list(set(exclusion for treatment in self.data['_default'].values() for eligibility in treatment['eligibility'] for exclusion in eligibility['exclusion']))
        self.exclusions = ctk.CTkLabel(master=self, text="Select exclusions that apply:")
        self.exclusions.grid(row=4, column=0, padx=10, pady=5)

        self.exclusion_checkboxes = {}
        for i, exclusion in enumerate(exclusions):
            cb = ctk.CTkCheckBox(master=self, text=exclusion)
            cb.grid(row=5 + i, column=0, sticky="nsew")
            self.exclusion_checkboxes[exclusion] = cb

        diseases = list(self.disease_to_severity.keys())
        self.diseases_label = ctk.CTkLabel(master=self, text="Select disease:")
        self.diseases_label.grid(row=10, column=0, padx=10, pady=5)
        self.disease_var = tk.StringVar()
        self.disease_dropdown = ctk.CTkOptionMenu(master=self, variable=self.disease_var, values=diseases, command=self.update_severity_dropdown)
        self.disease_dropdown.grid(row=10, column=1, padx=10, pady=5)

        self.severity_label = ctk.CTkLabel(master=self, text="Select severity:")
        self.severity_label.grid(row=11, column=0, padx=10, pady=5)
        self.severity_var = tk.StringVar()
        self.severity_dropdown = ctk.CTkOptionMenu(master=self, variable=self.severity_var, values=[])
        self.severity_dropdown.grid(row=11, column=1, padx=10, pady=5)

        self.display_textbox = ctk.CTkTextbox(master=self)
        self.display_textbox.grid(row=0, column=2, columnspan=2, rowspan=14, padx=10, pady=10, sticky="nsew")

        self.submit_button = ctk.CTkButton(master=self, text="Submit disease", command=self.submit_disease)
        self.submit_button.grid(row=14, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        
        self.button = ctk.CTkButton(master=self, text="Confirm Selection", command=self.button_callback)
        self.button.grid(row=15, column=0, columnspan=2, padx=10, pady=10, sticky="ew")


    def update_severity_dropdown(self, selected_disease):
        severities = self.disease_to_severity.get(selected_disease, [])
        # Delete the old severity dropdown and create a new one with the updated values
        self.severity_dropdown.destroy()
        self.severity_dropdown = ctk.CTkOptionMenu(master=self, variable=self.severity_var, values=severities)
        self.severity_dropdown.grid(row=11, column=1, padx=10, pady=5)
        if severities:
            self.severity_var.set(severities[0])
        else:
            self.severity_var.set('')


    def get_exclusions(self):
        selected_exclusions = []
        for exclusion, checkbox in self.exclusion_checkboxes.items():
            if checkbox.get() == 1:  # Adjusted for customtkinter
                selected_exclusions.append(exclusion)
        return selected_exclusions

    def submit_disease(self):
        disease = self.disease_dropdown.get()
        severity = self.severity_var.get()  # Use severity_var to get the current severity value
        # Update to include severity value correctly
        self.user_data["diseases"].append({"disease": disease, "severity": severity})
        print(self.user_data)  # This will now show the updated diseases list with severities

    def button_callback(self):
        self.user_data.update({
            "weight": self.weight_entry.get(),
            "height": self.height_entry.get(),
            "age": self.age_entry.get(),
            "exclusions": self.get_exclusions(),
            "cpg": self.cpg_dropdown.get()
        })
        print(self.user_data)  # For verification


if __name__ == "__main__":
    app = App()
    app.mainloop()




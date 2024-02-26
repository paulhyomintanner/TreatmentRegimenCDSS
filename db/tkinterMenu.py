import customtkinter as ctk
import json

class TreatmentApp:
    def __init__(self, root):
        self.root = root
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("dark-blue")
        self.setup_ui()

    def load_data(self):
        with open('testing_db.json') as f:
            data = json.load(f)
        return data

    def on_submit(self):
        self.weight = self.weight_entry.get()
        self.height = self.height_entry.get()
        self.disease = self.disease_dropdown.get()
        self.cpg = self.cpg_dropdown.get()
        self.severity = self.severity_dropdown.get()
        self.exclusion = self.exclusion_dropdown.get()

        self.user_data = {
            "weight": self.weight,
            "height": self.height,
            "disease": self.disease,
            "cpg": self.cpg,
            "severity": self.severity,
            "exclusion": self.exclusion
        }

        print(self.user_data)

    def setup_ui(self):
        self.root.title("Treatment Selection")
        self.root.geometry("400x600")

        data = self.load_data()
        diseases = list(set(treatment['disease'] for treatment in data['_default'].values()))
        cpgs = list(set(cpg for treatment in data['_default'].values() for cpg in treatment['rank'][0]))
        severity = list(set(eligibility['severity'] for treatment in data['_default'].values() for eligibility in treatment['eligibility']))
        exclusions = list(set(exclusion for treatment in data['_default'].values() for eligibility in treatment['eligibility'] for exclusion in eligibility['exclusion']))

        ctk.CTkLabel(self.root, text="Patient's weight in kg:").pack(pady=5)
        self.weight_entry = ctk.CTkEntry(self.root)
        self.weight_entry.pack(pady=5)

        ctk.CTkLabel(self.root, text="Patient's height in cm:").pack(pady=5)
        self.height_entry = ctk.CTkEntry(self.root)
        self.height_entry.pack(pady=5)

        ctk.CTkLabel(self.root, text="Select a disease:").pack(pady=5)
        self.disease_dropdown = ctk.CTkOptionMenu(self.root, values=diseases)
        self.disease_dropdown.pack(pady=5)

        ctk.CTkLabel(self.root, text="Select a CPG:").pack(pady=5)
        self.cpg_dropdown = ctk.CTkOptionMenu(self.root, values=cpgs)
        self.cpg_dropdown.pack(pady=5)

        ctk.CTkLabel(self.root, text="Select a severity:").pack(pady=5)
        self.severity_dropdown = ctk.CTkOptionMenu(self.root, values=severity)
        self.severity_dropdown.pack(pady=5)

        ctk.CTkLabel(self.root, text="Select an exclusion:").pack(pady=5)
        self.exclusion_dropdown = ctk.CTkOptionMenu(self.root, values=exclusions)
        self.exclusion_dropdown.pack(pady=5)

        self.submit_button = ctk.CTkButton(self.root, text="Submit", command=self.on_submit)
        self.submit_button.pack(pady=10)

def main():
    root = ctk.CTk()
    app = TreatmentApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

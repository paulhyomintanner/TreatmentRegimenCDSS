import customtkinter as ctk
import json

class TreatmentApp:
    def __init__(self, root):
        self.root = root
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("dark-blue")
        self.root.geometry("400x600")
        self.data = self.load_data()
        self.setup_page_one()

    def load_data(self):
        with open('testing_db.json') as f:
            data = json.load(f)
        return data

    def submit_page_one(self):
        self.weight = self.weight_entry.get()
        self.height = self.height_entry.get()
        self.age = self.age_entry.get()
        self.cpg = self.cpg_dropdown.get()
        self.exclusions = [text for text, cb in self.exclusion_checkboxes.items() if cb.get() == 1]
        self.page_one.pack_forget()  # Hide page one
        self.setup_page_two()  # Setup and show page two

    def submit_page_two(self):
        self.disease = self.disease_dropdown.get()
        self.severity = self.severity_dropdown.get()
        self.user_data = {
            "weight": self.weight,
            "height": self.height,
            "age": self.age, 
            "cpg": self.cpg,
            "disease": self.disease,
            "severity": self.severity,
            "exclusions": self.exclusions
        }
        print(self.user_data)
        # Here you can either show a confirmation, close the app, or return to the first page

    def setup_page_one(self):
        self.page_one = ctk.CTkFrame(self.root)
        self.page_one.pack(fill="both", expand=True)

        cpgs = list(set(cpg for treatment in self.data['_default'].values() for cpg in treatment['rank'][0]))
        exclusions = list(set(exclusion for treatment in self.data['_default'].values() for eligibility in treatment['eligibility'] for exclusion in eligibility['exclusion']))

        ctk.CTkLabel(self.page_one, text="Patient's weight in kg:").pack(pady=5)
        self.weight_entry = ctk.CTkEntry(self.page_one)
        self.weight_entry.pack(pady=5)

        ctk.CTkLabel(self.page_one, text="Patient's height in cm:").pack(pady=5)
        self.height_entry = ctk.CTkEntry(self.page_one)
        self.height_entry.pack(pady=5)

        ctk.CTkLabel(self.page_one, text="Patients age:").pack(pady=5)
        self.age_entry = ctk.CTkEntry(self.page_one)
        self.age_entry.pack(pady=5)

        ctk.CTkLabel(self.page_one, text="Select a CPG:").pack(pady=5)
        self.cpg_dropdown = ctk.CTkOptionMenu(self.page_one, values=cpgs)
        self.cpg_dropdown.pack(pady=5)
        
        ctk.CTkLabel(self.page_one, text="Select exclusions that apply:").pack(pady=5)
        self.exclusion_checkboxes = {}  # Dictionary to store checkboxes with their text as keys
        for exclusion in exclusions:
            cb = ctk.CTkCheckBox(self.page_one, text=exclusion)
            cb.pack(anchor="w", pady=2)
            self.exclusion_checkboxes[exclusion] = cb

        ctk.CTkButton(self.page_one, text="Next", command=self.submit_page_one).pack(pady=10)

    def setup_page_two(self):
        self.page_two = ctk.CTkFrame(self.root)
        self.page_two.pack(fill="both", expand=True)

        diseases = list(set(treatment['disease'] for treatment in self.data['_default'].values()))
        severity = list(set(eligibility['severity'] for treatment in self.data['_default'].values() for eligibility in treatment['eligibility']))

        ctk.CTkLabel(self.page_two, text="Select a disease:").pack(pady=5)
        self.disease_dropdown = ctk.CTkOptionMenu(self.page_two, values=diseases)
        self.disease_dropdown.pack(pady=5)

        ctk.CTkLabel(self.page_two, text="Select a severity:").pack(pady=5)
        self.severity_dropdown = ctk.CTkOptionMenu(self.page_two, values=severity)
        self.severity_dropdown.pack(pady=5)

        ctk.CTkLabel(self.page_two, text="Click submit for each disease").pack(pady=5)
        ctk.CTkButton(self.page_two, text="Submit", command=self.submit_page_two).pack(pady=10)


    def on_submit(self):
        self.weight = float(self.weight_entry.get())
        self.height = float(self.height_entry.get())
        self.disease = self.disease_dropdown.get()
        self.cpg = self.cpg_dropdown.get()
        self.severity = self.severity_dropdown.get()
        self.exclusion = self.exclusion_dropdown.get().split(',')

        self.user_data = {
            "weight": self.weight,
            "height": self.height,
            "disease": self.disease,
            "cpg": self.cpg,
            "severity": self.severity,
            "exclusion": self.exclusion
        }

        data = self.load_data()
        treatments = list(data['_default'].values())
        treatments_for_disease = self.filter_by_disease(treatments, self.disease)
        treatments_for_severity = self.filter_by_severity(treatments_for_disease, self.severity)
        treatments_excluding_exclusions = self.filter_by_exclusions(treatments_for_severity, self.exclusion)
        treatments_for_patient_profile = self.filter_patient_profile(treatments_excluding_exclusions, self.age, self.weight)
        ranked_treatments = self.rank_treatments(treatments_for_patient_profile, self.cpg)

        print(ranked_treatments)

    def filter_by_disease(self, treatments, diagnosis):
        return [treatment for treatment in treatments if treatment['disease'].lower() == diagnosis.lower()]

    def filter_by_severity(self, treatments, severity):
        return [treatment for treatment in treatments for eligibility in treatment['eligibility'] if eligibility['severity'].lower() == severity.lower()]
    
    def filter_by_exclusions(self, treatments, exclusions):
        exclusions = [exclusion.strip().lower() for exclusion in exclusions if exclusion.strip()]
        return [treatment for treatment in treatments if not any(
            any(exclusion in eligibility.get('exclusion', []) for exclusion in exclusions)
            for eligibility in treatment['eligibility']
        )]

    def filter_patient_profile(self, treatments, age, weight):
        return [treatment for treatment in treatments for eligibility in treatment['eligibility'] if eligibility['patient_profile']['age_range']['min'] <= age <= eligibility['patient_profile']['age_range']['max'] and weight >= eligibility['patient_profile']['min_weight']]

    def rank_treatments(self, treatments, preferred_cpg):
        return sorted(treatments, key=lambda x: x['rank'][0][preferred_cpg])  


def main():
    root = ctk.CTk()
    app = TreatmentApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
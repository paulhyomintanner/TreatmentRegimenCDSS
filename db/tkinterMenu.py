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

        self.user_data = {
        "weight": None,
        "height": None,
        "age": None, 
        "cpg": None,
        "diseases": [],
        "exclusions": []
    }

    def load_data(self):
        with open('testing_db.json') as f:
            data = json.load(f)
        return data

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
        age = int(age)
        weight = int(weight)
        return [treatment for treatment in treatments for eligibility in treatment['eligibility'] if eligibility['patient_profile']['age_range']['min'] <= age <= eligibility['patient_profile']['age_range']['max'] and weight >= eligibility['patient_profile']['min_weight']]

    def rank_treatments(self, treatments, preferred_cpg):
        return sorted(treatments, key=lambda x: x['rank'][0][preferred_cpg])


    def submit_page_one(self):
        self.user_data["weight"] = self.weight_entry.get()
        self.user_data["height"] = self.height_entry.get()
        self.user_data["age"] = self.age_entry.get()
        self.user_data["cpg"] = self.cpg_dropdown.get()
        self.user_data["exclusions"] = [text for text, cb in self.exclusion_checkboxes.items() if cb.get() == 1]
        self.page_one.pack_forget()  
        self.setup_page_two()  

    def submit_page_two(self):
        disease = self.disease_dropdown.get()
        severity = self.severity_dropdown.get()
        self.user_data["diseases"].append({"disease": disease, "severity": severity})
        print(self.user_data)

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
        ctk.CTkButton(self.page_two, text="Retrieve Treatments", command=self.retrieve_treatments).pack(pady=10)

    def retrieve_treatments(self):
        treatments = self.data['_default'].values()
        for disease_info in self.user_data["diseases"]:
            disease_treatments = self.filter_by_disease(treatments, disease_info["disease"])
            severity_treatments = self.filter_by_severity(disease_treatments, disease_info["severity"])
            exclusion_treatments = self.filter_by_exclusions(severity_treatments, self.user_data["exclusions"])
            profile_treatments = self.filter_patient_profile(exclusion_treatments, self.user_data["age"], self.user_data["weight"])
            ranked_treatments = self.rank_treatments(profile_treatments, self.user_data["cpg"])
            if ranked_treatments:
                treatment = ranked_treatments[0]
                treatment_id = treatment['treatment_id']
                description = treatment['description']
                drugs = ', '.join([medication['drug'] for medication in treatment['medication']])
                medication_details = ', '.join([f"{key}: {value}" for medication in treatment['medication'] for key, value in medication.items() if key in ["drug", "form", "site", "route", "method"]])
                treatment_text = f"Recommended treatment for {disease_info['disease']}:\nTreatment ID: {treatment_id}\nDescription: {description}\nDrugs: {drugs}\nMedication Details: {medication_details}\n"
            else:
                treatment_text = "No treatment found for this disease"
            ctk.CTkLabel(self.page_two, text=treatment_text).pack(pady=10)

        ctk.CTkButton(self.page_two, text="Retrieve Treatments", command=self.retrieve_treatments).pack(pady=10)


def main():
    root = ctk.CTk()
    app = TreatmentApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
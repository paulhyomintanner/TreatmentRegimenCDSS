import customtkinter as ctk
import json
from tkinter import messagebox
import tkinter as tk
import math


class TreatmentApp:
    def __init__(self, root):
        self.root = root
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("dark-blue")
        self.root.geometry("500x800")
        self.data = self.load_data()
        self.setup_page_one()
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

    def return_to_page_one(self):
        self.page_two.pack_forget()
        self.reset_data()
        self.setup_page_one()
    
    def load_data(self):
        with open('dosing_db.json') as f:
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
        return [treatment for treatment in treatments for eligibility in treatment['eligibility'] 
                if eligibility['patient_profile']['age_range']['min'] <= age <= eligibility['patient_profile']['age_range']['max'] 
                and weight >= eligibility['patient_profile']['min_weight']]

    def rank_treatments(self, treatments, preferred_cpg):
        return sorted(treatments, key=lambda x: x['rank'][0][preferred_cpg])

    def submit_page_one(self):
        try:
            self.user_data["weight"] = int(self.weight_entry.get())
            self.user_data["height"] = int(self.height_entry.get())
            self.user_data["age"] = int(self.age_entry.get())
        except ValueError:
            print("Please enter a valid number for weight, height, and age.")
            return
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
        self.exclusion_checkboxes = {}  
        for exclusion in exclusions:
            cb = ctk.CTkCheckBox(self.page_one, text=exclusion)
            cb.pack(anchor="w", pady=2)
            self.exclusion_checkboxes[exclusion] = cb

        ctk.CTkButton(self.page_one, text="Next", command=self.submit_page_one).pack(pady=10)

    def setup_page_two(self):
        self.page_two = ctk.CTkFrame(self.root)
        self.page_two.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(self.page_two)  
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.configure(bg='#2D2D2D') 

        scrollbar = tk.Scrollbar(self.page_two, bg='#2D2D2D', troughcolor='#4D4D4D', activebackground='#4D4D4D', command=self.canvas.yview)
        scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.inner_frame = tk.Frame(self.canvas, bg='#2D2D2D')  
        self.canvas.create_window((0,   0), window=self.inner_frame, anchor="nw")

        diseases = list(set(treatment['disease'] for treatment in self.data['_default'].values()))
        severity = list(set(eligibility['severity'] for treatment in self.data['_default'].values() for eligibility in treatment['eligibility']))

        ctk.CTkLabel(self.inner_frame, text="Select a disease:").pack(pady=5)
        self.disease_dropdown = ctk.CTkOptionMenu(self.inner_frame, values=diseases)
        self.disease_dropdown.pack(pady=5)

        ctk.CTkLabel(self.inner_frame, text="Select a severity:").pack(pady=5)
        self.severity_dropdown = ctk.CTkOptionMenu(self.inner_frame, values=severity)
        self.severity_dropdown.pack(pady=5)

        ctk.CTkLabel(self.inner_frame, text="Click submit for each disease").pack(pady=5)
        ctk.CTkButton(self.inner_frame, text="Submit", command=self.submit_page_two).pack(pady=10)
        ctk.CTkButton(self.inner_frame, text="Retrieve Treatments", command=self.retrieve_treatments).pack(pady=10)
        ctk.CTkButton(self.inner_frame, text="Return to Start", command=self.return_to_page_one).pack(pady=10)

        self.canvas.update_idletasks() 
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    
    def load_superseding_rules(self):
        with open('superseding_rules_db.json') as f:
            rules = json.load(f)
        return rules["_default"]

    def retrieve_treatments(self):
        if not self.user_data or not self.user_data['weight'] or not self.user_data['height'] or not self.user_data['age']:
            messagebox.showerror("Error", "Please fill in all the necessary inputs before retrieving treatments.")
            return
        while True:
            treatments = self.data['_default'].values()
            candidate_treatments = {}
            for disease_info in self.user_data["diseases"]:
                disease_treatments = self.filter_by_disease(treatments, disease_info["disease"])
                severity_treatments = self.filter_by_severity(disease_treatments, disease_info["severity"])
                exclusion_treatments = self.filter_by_exclusions(severity_treatments, self.user_data["exclusions"])
                profile_treatments = self.filter_patient_profile(exclusion_treatments, self.user_data["age"], self.user_data["weight"])
                profile_treatments = [treatment for treatment in profile_treatments if treatment['treatment_id'] not in self.rejected_treatments]
                ranked_treatments = self.rank_treatments(profile_treatments, self.user_data["cpg"])
                
                if ranked_treatments:
                    candidate_treatments[disease_info["disease"]] = ranked_treatments[0]
                else:
                    no_treatment_text = f"No treatments found for {disease_info['disease']}"
                    ctk.CTkLabel(self.inner_frame, text=no_treatment_text).pack(pady=10)
            
            if not candidate_treatments:
                ctk.CTkLabel(self.inner_frame, text="No treatments found for any diseases.").pack(pady=10)
                break

            self.root.update_idletasks()  
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))
            recommended_treatments = {}
            
            if candidate_treatments:
                recommended_treatments = self.rules(candidate_treatments)

            for disease, treatment in recommended_treatments.items():
                medication_details = ', '.join([f"{key}: {value}" for medication in treatment['medication'] for key, value in medication.items() if key in ["drug", "form", "site", "route", "method"]])
                treatment_text = f"Recommended treatment for {disease}:\nTreatment ID: {treatment['treatment_id']}\nDescription: {treatment['description']}\nMedication details: {medication_details}"
                ctk.CTkLabel(self.inner_frame, text=treatment_text).pack(pady=10)

            if not recommended_treatments:
                ctk.CTkLabel(self.inner_frame, text="No recommended treatments after applying rules.").pack(pady=10)

            ctk.CTkButton(self.inner_frame, text="Confirm Treatments", command=self.confirm_treatments).pack(pady=10)
            ctk.CTkButton(self.inner_frame, text="Reject Treatment", command=self.reject_treatment_ui).pack(pady=10)

            self.root.update_idletasks()  
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))

            self.recommended_treatments = recommended_treatments   
            if self.recommended_treatments:
                break

   
    def handle_rejection(self):
        rejected_ids = self.reject_entry.get().split(',')  
        self.user_data['exclusions'].extend(rejected_ids)  
        self.rejected_treatments.extend(rejected_ids)  
        self.page_two.pack_forget()
        self.setup_page_two()
        self.retrieve_treatments()  

    def rules(self, candidate_treatments):
        superseding_rules = self.load_superseding_rules()
        recommended_treatments = {}
        for disease, treatment in candidate_treatments.items():
            treatment_id = treatment['treatment_id']
            for rule in superseding_rules.values():
                if treatment_id in rule["pair"]:
                    superseding_id = rule["superseding_id"]
                    for d, t in candidate_treatments.items():
                        if t['treatment_id'] == superseding_id:
                            recommended_treatments[disease] = t
                            break
                    else:
                        recommended_treatments[disease] = treatment
                    break
            else:
                recommended_treatments[disease] = treatment

        for disease, treatment in candidate_treatments.items():
            treatment_id = treatment['treatment_id']
            for rule in superseding_rules.values():
                if treatment_id in rule["pair"]:
                    superseding_id = rule["superseding_id"]
                    for d, t in candidate_treatments.items():
                        if t['treatment_id'] == superseding_id:
                            recommended_treatments[disease] = t
                            break
        return recommended_treatments

    def confirm_treatments(self):
        for disease, treatment in self.recommended_treatments.items():
            treatment_text = f"Recommended treatment for {disease}:\nTreatment ID: {treatment['treatment_id']}\nDescription: {treatment['description']}"
            ctk.CTkLabel(self.inner_frame, text=treatment_text).pack(pady=10)

            for medication in treatment['medication']:
                medication_details = ', '.join([f"{key}: {value}" for key, value in medication.items() if key in ["drug", "form", "site", "route", "method"]])
                dose_strategy = medication['dose_strategy']
                instruction = dose_strategy['text']
                additional_instruction = dose_strategy['additionalInstruction'][0]['text']
                patient_instruction = dose_strategy['patientInstruction']
                max_dose = dose_strategy['maxDosePerPeriod']['numerator']['value']
                max_dose_unit = dose_strategy['maxDosePerPeriod']['numerator']['unit']
                period = dose_strategy['maxDosePerPeriod']['denominator']['value']
                period_unit = dose_strategy['maxDosePerPeriod']['denominator']['unit']

                medication_text = f"Medication details: {medication_details}\nInstruction: {instruction}\nAdditional instruction: {additional_instruction}\nPatient instruction: {patient_instruction}\nMax dose: {max_dose} {max_dose_unit} per {period} {period_unit}"
                ctk.CTkLabel(self.inner_frame, text=medication_text).pack(pady=10)
            
            for widget in self.inner_frame.winfo_children():
                widget.destroy()
                
        self.root.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
            

        self.check_calculations()

    def reject_treatment_ui(self):
        self.reject_entry = ctk.CTkEntry(self.inner_frame, placeholder_text="Type ID or IDs to reject")
        self.reject_entry.pack(pady=5)
        ctk.CTkButton(self.inner_frame, text="Confirm Rejection", command=self.handle_rejection).pack(pady=10)

    def check_calculations(self):
        for treatment in self.recommended_treatments.values():
            for medication in treatment['medication']:
                dose_strategy = medication.get('dose_strategy', {})
                calculation = dose_strategy.get('calculation')
                if calculation in ['bsa', 'weight']:
                    checkbox = ctk.CTkCheckBox(self.inner_frame, text=f"Recommended calculation: {calculation} calculation available for {medication['drug']}\n Select to calculate dose")                 
                    checkbox.pack()

                    form = medication.get('form', {})
                    divisible = form.get('divisible')
                    if divisible:
                        input_box = ctk.CTkEntry(self.inner_frame, placeholder_text="Input concentration of medication per unit (mg/ml, mg/tablet)")
                        input_box.pack()
        
        
        
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))




def main():
    root = ctk.CTk()
    app = TreatmentApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()




import tkinter as tk
from tkinter import simpledialog
from tinydb import TinyDB
import math

db = TinyDB('testing_db.json')
all_treatments = db.all()


def filter_by_disease(treatments, diagnosis):
    return [treatment for treatment in treatments 
            if treatment['disease'].lower() == diagnosis.lower()]

def filter_by_severity(treatments, severity):
    return [treatment for treatment in treatments for eligibility in treatment['eligibility'] 
            if eligibility['severity'].lower() == severity.lower()]

def filter_by_exclusions(treatments, exclusions):
    exclusions = [exclusion.strip().lower() for exclusion in exclusions if exclusion.strip()]
    return [treatment for treatment in treatments 
            if not any(any(exclusion in eligibility.get('exclusion', []) 
                           for exclusion in exclusions) for eligibility in treatment['eligibility'])]

def filter_patient_profile(treatments, age, weight):
    return [treatment for treatment in treatments for eligibility in treatment['eligibility']
            if eligibility['patient_profile']['age_range']['min'] <= age <= eligibility['patient_profile']['age_range']['max'] 
            and weight >= eligibility['patient_profile']['min_weight']]

def rank_treatments(treatments, preferred_cpg):
    return sorted(treatments, key=lambda x: x['rank'][0][preferred_cpg])

def rules(treatments_by_disease):
    db = TinyDB('superseding_rules_db.json')
    rules = db.all()

    top_treatments = {}

    for disease, treatments in treatments_by_disease.items():
        if treatments:  
            top_treatments[disease] = treatments[0]['treatment_id']
    
    recommended_treatments = {}

    for rule in rules:
        rule_pair = rule['pair']
        superseding_id = rule['superseding_id']

        if set(rule_pair) == set(top_treatments.values()):
            for disease, treatment_id in top_treatments.items():
                if treatment_id == superseding_id:
                    superseding_treatment = treatments_by_disease[disease][0]
                    recommended_treatments[disease] = superseding_treatment
                    return recommended_treatments  
    
    for disease, treatment in top_treatments.items():
        if disease in treatments_by_disease and treatments_by_disease[disease]:  
            recommended_treatments[disease] = treatments_by_disease[disease][0]

    return recommended_treatments

def calculate_bsa(height_cm, weight_kg):
    # Calculate the Body Surface Area using the Mosteller formula
    return math.sqrt((height_cm * weight_kg) / 3600)

def calculate_dose_based_on_weight(weight_kg, dose_mg_per_kg):
    return weight_kg * dose_mg_per_kg

def calculate_dose_based_on_bsa(bsa_m2, dose_mg_per_m2):
    return bsa_m2 * dose_mg_per_m2

def check_max_dose(calculated_dose, max_dose):
    if calculated_dose > max_dose:
        return max_dose
    return calculated_dose

def calculate_dose_per_administration(total_dose, frequency):
    return total_dose / frequency

def main():
    root = tk.Tk()
    root.withdraw()  

    preferred_cpg = simpledialog.askstring("Input", "Preferred CPG (WHO/BNF):")
    exclusions = simpledialog.askstring("Input", "Exclusions e.g allergy (comma-separated):")
    if exclusions is not None:
        exclusions = exclusions.split(',')
    weight = simpledialog.askfloat("Input", "Enter the patient's weight in kg:")
    height = simpledialog.askfloat("Input", "Enter the patient's height in cm:")
    age = simpledialog.askfloat("Input", "Enter the patient's age in years:")

    diseases = []
    while True:
        disease = simpledialog.askstring("Input", "Add diagnosis (name):")
        if not disease:
            break
        severity = simpledialog.askstring("Input", "Diagnosis severity (low/high):")
        diseases.append({'name': disease, 'severity': severity})
        add_extra_disease = simpledialog.askstring("Input", "Add another disease? (yes/no):")
        if add_extra_disease.lower() != "yes":
            break
    user_input = ''

    while True:
        no_treatments_left = True   

        for disease_info in diseases:
            treatments_for_disease = filter_by_disease(all_treatments, disease_info['name'])
            treatments_for_severity = filter_by_severity(treatments_for_disease, disease_info['severity'])
            treatments_excluding_exclusions = filter_by_exclusions(treatments_for_severity, exclusions)
            treatments_for_patient_profile = filter_patient_profile(treatments_excluding_exclusions, age, weight)
            ranked_treatments = [treatment for treatment in rank_treatments(treatments_for_patient_profile, preferred_cpg) if treatment not in rejected_treatments]

            treatments_by_disease[disease_info['name']] = ranked_treatments

            if ranked_treatments:
                no_treatments_left = False   

            else:
                print(f"No treatments found for {disease_info['name']} after applying exclusions and rejections.")

        if no_treatments_left:
            print("No treatments available for all diseases after applying exclusions and rejections.")
            break   

        recommended_treatments = rules(treatments_by_disease)
        for disease, treatment in recommended_treatments.items():
            treatment_id = treatment['treatment_id']
            description = treatment['description']
            drugs = ', '.join([medication['drug'] for medication in treatment['medication']])
            medication_details = ', '.join([f"{key}: {value}" for medication in treatment['medication'] for key, value in medication.items() if key in ["drug", "form", "site", "route", "method"]])
            print(f"Recommended treatment for {disease}: Treatment ID: {treatment_id}, Description: {description}, Drugs: {drugs}, Medication Details: {medication_details}")
            

        user_input = input("Do you accept the recommended treatment? (yes/no): ").strip().lower()
        if user_input == 'yes':
            break   
        else:
            rejected_treatment_ids = input("Enter treatment IDs for rejection (separated by commas): ").strip().split(',')
            for rejected_treatment_id in rejected_treatment_ids:
                rejected_treatment_id = rejected_treatment_id.strip()   
                for treatments in treatments_by_disease.values():
                    for treatment in treatments:
                        if treatment['treatment_id'] == rejected_treatment_id:
                            rejected_treatments.append(treatment)
                            break

    confirmed_treatment = None

    if user_input == 'yes':
        print("You have accepted the following treatment plan:")
        confirmed_treatment = {}
        for disease, treatments in recommended_treatments.items():
            if treatments:   
                treatment_id = treatments['treatment_id']
                description = treatments['description']
                drugs = ', '.join([medication['drug'] for medication in treatments['medication']])
                medication_details = ', '.join([f"{key}: {value}" for medication in treatments['medication'] for key, value in medication.items() if key in ["drug", "form", "site", "route", "method"]])
                print(f"{disease} - Confirmed treatment ID: {treatment_id}, Description: {description}, Drugs: {drugs}, Medication Details: {medication_details}")
                confirmed_treatment[disease] = treatments
            else:
                print(f"No treatments available for {disease} after applying exclusions and rejections.")

    if confirmed_treatment:
        for disease, treatment in confirmed_treatment.items():
            for medication in treatment['medication']:
                if medication['dose_strategy'].get("calculation") == "yes": 
                    calculate_dose_option = input(f"Calculate dose for {medication['drug']} according to CPG provided formular? (yes/no): ").strip().lower()
                    if calculate_dose_option == 'yes':
                        dose_and_rate = medication['dose_strategy']['doseAndRate'][0]
                        dose_quantity = dose_and_rate['doseQuantity']['value']
                        unit = dose_and_rate['doseQuantity']['unit']
                        frequency = medication['dose_strategy']['timing']['repeat']['frequency']
                        max_dose = medication['dose_strategy']['maxDosePerPeriod']['numerator']['value']

                        if unit == 'mg/kg':
                            total_dose = calculate_dose_based_on_weight(weight, dose_quantity)
                        elif unit == 'mg/m^2':
                            bsa = calculate_bsa(height, weight)
                            total_dose = calculate_dose_based_on_bsa(bsa, dose_quantity)
                        else:
                            raise ValueError("Unknown dosing unit.")

                        total_dose = check_max_dose(total_dose, max_dose)
                        dose_per_administration = calculate_dose_per_administration(total_dose, frequency)

                        print(f"The calculated dose per administration is: {dose_per_administration}mg")

                        calculate_volume = input("Do you want to calculate the volume per dose? (yes/no): ").strip().lower()
                        if calculate_volume == 'yes':
                            concentration = float(input("Enter the drug concentration per unit (mg/ml or mg/tablet): "))
                            volume_per_dose = dose_per_administration / concentration
                            print(f"The volume per dose needed is: {volume_per_dose} units")
                    else:
                        print(f"No dose calculation requested {medication}.")               
                else:
                    print(f"No dose calculation in plan {medication}.")
if __name__ == "__main__":
    main()

    root.mainloop()



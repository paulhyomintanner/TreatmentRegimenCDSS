import flet as ft
import json
from tinydb import TinyDB
db = TinyDB('testing_db.json')
all_treatments = db.all()
import math 

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

def calculate_bsa(height_cm, weight_kg):    # Calculate the Body Surface Area using the Mosteller formula
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


def main(page: ft.Page):
    page.title = "Disease Selection"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Load the JSON file
    with open('testing_db.json') as f:
        data = json.load(f)

    # Extract the diseases from the JSON data
    diseases = list(set(treatment['disease'] for treatment in data['_default'].values()))
    cpgs = list(set(cpg for treatment in data['_default'].values() for cpg in treatment['rank'][0]))
    severity = list(set(eligibility['severity'] for treatment in data['_default'].values() for eligibility in treatment['eligibility']))
    exclusions = list(set(exclusion for treatment in data['_default'].values() for eligibility in treatment['eligibility'] for exclusion in eligibility['exclusion']))
    
    
    

    weight_textfield = ft.TextField(
        label="Enter the patient's weight in kg",
        input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9\.]", replacement_string=""))
    
    #confirm_weight_button = ft.FilledButton(text="Confirm")

    height_textfield = ft.TextField(
        label="Enter the patient's height in cm",
        input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9\.]", replacement_string=""))
    
    #confirm_height_buttom = ft.FilledButton(text="Confirm")

    disease_dropdown = ft.Dropdown(
        label="Select a disease",
        options=[ft.dropdown.Option(text=disease) for disease in diseases]  
    )
    cpg_dropdown = ft.Dropdown(
        label="Select a CPG",
        options=[ft.dropdown.Option(text=cpg) for cpg in cpgs]
    )
    severity_dropdown = ft.Dropdown(
        label="Select a severity",
        options=[ft.dropdown.Option(text=severity) for severity in severity]
    )
    exclusions_dropdown = ft.Dropdown(
        label="Select an exclusion",
        options=[ft.dropdown.Option(text=exclusion) for exclusion in exclusions]
    )


    def disease_selected(e):
        selected_disease = disease_dropdown.value
        print(f"Selected Disease: {selected_disease}")  

    def cpg_selected(e):
        selected_cpg = cpg_dropdown.value
        print(f"Selected CPG: {selected_cpg}")
    
    def severity_selected(e):
        selected_severity = severity_dropdown.value
        print(f"Selected Severity: {selected_severity}")

    def exclusions_selected(e):
        selected_exclusions = exclusions_dropdown.value
        print(f"Selected Exclusions: {selected_exclusions}")

    def weight(e):
        if weight_textfield.value:
            weight = float(weight_textfield.value)
            print(f"Weight: {weight} kg")

    def confirm_weight(e):
        if weight_textfield.value:
            weight = float(weight_textfield.value)
            print(f"Weight: {weight} kg")

    def height(e):
        if height_textfield.value:
            height = float(height_textfield.value)
            print(f"Height: {height} cm")

    def confirm_height(e):
        if height_textfield.value:
            height = float(height_textfield.value)
            print(f"Height: {height} cm")

    severity_dropdown.on_change = severity_selected
    exclusions_dropdown.on_change = exclusions_selected
    cpg_dropdown.on_change = cpg_selected
    disease_dropdown.on_change = disease_selected
    weight_textfield.on_submit = weight
    height_textfield.on_submit = height
    #confirm_weight_button.on_click = confirm_weight
    #confirm_height_buttom.on_click = confirm_height


    page.add(disease_dropdown, cpg_dropdown, severity_dropdown, exclusions_dropdown, weight_textfield, height_textfield)

#confirm_weight_button, confirm_height_buttom
    
ft.app(target=main)
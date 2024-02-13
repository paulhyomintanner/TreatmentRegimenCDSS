from tinydb import TinyDB

# Primary filter for treatments. 
def filter_by_disease(treatments, diagnosis):
    diagnosis = diagnosis.lower()  
    return [treatment for treatment in treatments if treatment['disease'].lower() == diagnosis]  # Normalized the input and list to lowercase

def filter_by_severity(treatments, severity):  #filter based on severity - technically could be any measure. 
    severity = severity.lower()  
    return [treatment for treatment in treatments if treatment['severity'].lower() == severity]  

def filter_by_exclusions(treatments, exclusions):
    exclusions = [exclusion.strip().lower() for exclusion in exclusions if exclusion.strip()]

    filtered_treatments = []
    for treatment in treatments:
        medication_list = treatment['medication']
        exclude_treatment = False

        for med in medication_list:
            med_exclusions = [ex.lower() for ex in med.get('exclusion', [])]  
            if any(exclusion in med_exclusions for exclusion in exclusions):
                exclude_treatment = True
                break  # Break the loop if any exclusion matches

        if not exclude_treatment:
            filtered_treatments.append(treatment)

    return filtered_treatments

# Enters the rank attribute dictionary and finds the corresponding ranking based on theCPG. 
def rank_treatments(treatments, preferred_cpg):
    return sorted(treatments, key=lambda x: x['rank'][0][preferred_cpg])

#Handles the user exclusions using the ID of the treatment to delete it from the list. 
def exclude_treatments(treatments):
    excluded_ids = input("Enter treatment IDs to exclude (comma-separated): ").strip().split(',')
    excluded_ids = [id.strip().upper() for id in excluded_ids]  # Normalize input IDs
    return [treatment for treatment in treatments if treatment['treatment_id'] not in excluded_ids]

# Updated function to print treatments with their IDs
def print_treatments(treatments, diagnosis):
    print(f"\nTreatments for {diagnosis}:")
    for treatment in treatments:
        print(f"ID: {treatment['treatment_id']}, Treatment: {treatment}")


# Handles the functions dealing with the evaluation of the treatments.
def evaluate_treatments(treatments, disease, severity, exclusions, preferred_cpg):
    treatments = filter_by_disease(treatments, disease) #primary filter
    treatments = filter_by_exclusions(treatments, exclusions) #eligibility section
    treatments = filter_by_severity(treatments, severity) #eligiblity section
    ranked_treatments = rank_treatments(treatments, preferred_cpg) #rank the treatments for user exclusion
    print_treatments(ranked_treatments, disease)
    updated_treatments = exclude_treatments(ranked_treatments)
    ranked_treatments = rank_treatments(updated_treatments, preferred_cpg) # rank the treatments after the user exclusion
    return ranked_treatments

def superseding_rules(ranked_treatments_diagnosis, ranked_treatments_comorbidity):
    if not ranked_treatments_comorbidity:
        print(f"Top treatment for diagnosis: {ranked_treatments_diagnosis[0]}")
        return

    # Select the top treatments from both lists
    top_diagnosis_treatment = ranked_treatments_diagnosis[0]
    top_comorbidity_treatment = ranked_treatments_comorbidity[0]

    # Open the rules database and retrieve all rules
    db = TinyDB('flexible_rules_db.json')
    rules = db.all()

    # Check if the top treatments match any rule
    for rule in rules:
        if set(rule['pair']) == set([top_diagnosis_treatment['treatment_id'], top_comorbidity_treatment['treatment_id']]):
            # If a match is found, print the superseding treatment and return
            superseding_treatment = top_diagnosis_treatment if rule['superseding_id'] == top_diagnosis_treatment['treatment_id'] else top_comorbidity_treatment
            print(f"Superseding treatment: {superseding_treatment}")
            return

    # If no match is found, print both top treatments
    print(f"Top treatments:\nDiagnosis: {top_diagnosis_treatment}\nComorbidity: {top_comorbidity_treatment}") 

def main():
    db = TinyDB('treatment_db.json')
    all_treatments = db.all() # Open the database and retrieve all treatments once

    # Get user inputs from console
    preferred_cpg = input("Preferred CPG (WHO/NICE): ").strip()
    exclusions = input("Exclusions (comma-separated): ").strip().split(',')
    primary_diagnosis = input("Primary diagnosis: ").strip()
    severity = input("Primary diagnosis severity (low/high): ").strip()
    has_comorbidity = input("Comorbidity? (yes/no): ").strip().lower() == "yes"

    ranked_treatments_diagnosis = evaluate_treatments(all_treatments, primary_diagnosis, severity, exclusions, preferred_cpg)
    ranked_treatments_comorbidity = None
    
    if has_comorbidity:
            comorbidity = input("Comorbidity name: ").strip()
            comorbidity_severity = input("Comorbidity severity (low/high): ").strip()
            ranked_treatments_comorbidity = evaluate_treatments(all_treatments, comorbidity, comorbidity_severity, exclusions, preferred_cpg)

    superseding_rules(ranked_treatments_diagnosis, ranked_treatments_comorbidity) # call the superseding rules function and pass the lists  as arguments

if __name__ == "__main__":
    main()
    
"""
Adds the rules for superceding in the rules_db.json and tiny db. Then selects the top treatments and prints them for now. It also ranks the 
treatments for exclusion accordning to the user inputted CPG. This corresponds to a rank that each treatment has per CPG. For now there is WHO and NICE
guidelines that are used. The lower the number the higher the rank. 
The next step would be the treatment validation and the regimen builder. The next stage would be to refactor the code into 
different modules for clarity and maintaibility. 
Process is as follows:

1. Primary filter applied using the disease from the user input.
2. Eligiblity criteria: exclusion and severity filters applied.
3. Ranking of treatments based on CPG.
4. User exclusion
5. Treatments re-ranked after the user exclusion.
6. Superseding rules applied.
7. Top treatments printed or treatment if rules are applied.
"""
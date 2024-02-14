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
    db = TinyDB('superseding_rules_db.json')
    rules = db.all()

    # Check if the top treatments match any rule
    for rule in rules:
        if set(rule['pair']) == set([top_diagnosis_treatment['treatment_id'], top_comorbidity_treatment['treatment_id']]):
            # If a match is found, print the superseding treatment and return
            superseding_treatment = top_diagnosis_treatment if rule['superseding_id'] == top_diagnosis_treatment['treatment_id'] else top_comorbidity_treatment
            print(f"\nSuperseding treatment: {superseding_treatment}")
            return [superseding_treatment]

    # If no match is found, print both top treatments
    print(f"\nTop treatments:\nDiagnosis: {top_diagnosis_treatment}\nComorbidity: {top_comorbidity_treatment}") 
    return [top_diagnosis_treatment, top_comorbidity_treatment]

def regimen_builder(treatments, dosing_strategy, patient_weight):
    for treatment in treatments:
        print(f"\nTreatment ID: {treatment['treatment_id']}, Drug: {treatment['medication'][0]['drug']}")
        for guideline in treatment['medication'][0]['dose_guideline']:
            if dosing_strategy in guideline:
                if dosing_strategy == 'standard':
                    print(f"Dosing Strategy: {dosing_strategy}, Dose (mg): {guideline[dosing_strategy][0]['dose_mg']}, Frequency per day: {guideline[dosing_strategy][0]['frequency_per_day']}")
                else:
                    dose_per_kg = guideline[dosing_strategy][0]['mg/kg']
                    frequency = guideline[dosing_strategy][0]['frequency_per_day']
                    daily_dose = patient_weight * dose_per_kg
                    single_dose = daily_dose / frequency
                    print(f"Dosing Strategy: {dosing_strategy}, Daily Dose (mg): {daily_dose}, Single Dose (mg): {single_dose}, Frequency per day: {frequency}")


def main():
    db = TinyDB('treatment_db.json')
    all_treatments = db.all()

    preferred_cpg = input("Preferred CPG (WHO/NICE): ").strip()
    exclusions = input("Exclusions (comma-separated): ").strip().split(',')
    primary_diagnosis = input("Primary diagnosis: ").strip()
    severity = input("Primary diagnosis severity (low/high): ").strip()
    has_comorbidity = input("Comorbidity? (yes/no): ").strip().lower() == "yes"

    ranked_treatments_diagnosis = evaluate_treatments(all_treatments, primary_diagnosis, severity, exclusions, preferred_cpg)
    print("\nRanked treatments after user exclusion:")
    print_treatments(ranked_treatments_diagnosis, primary_diagnosis)
    ranked_treatments_comorbidity = None

    if has_comorbidity:
        comorbidity = input("Comorbidity name: ").strip()
        comorbidity_severity = input("Comorbidity severity (low/high): ").strip()
        ranked_treatments_comorbidity = evaluate_treatments(all_treatments, comorbidity, comorbidity_severity, exclusions, preferred_cpg)
        print("\nRanked treatments after user exclusion:")
        print_treatments(ranked_treatments_comorbidity, comorbidity)
        treatments_to_use = superseding_rules(ranked_treatments_diagnosis, ranked_treatments_comorbidity)
    else:
        # No comorbidity, so use only the top treatment from diagnosis treatments
        treatments_to_use = [ranked_treatments_diagnosis[0]] if ranked_treatments_diagnosis else []

    validate = input("\nSelect highest ranked treatment/s (or superseding treatment) for dosing? (yes/no): ").strip().lower()
    if validate == 'yes':
        dosing_strategy = input("\nSelect dose guideline (standard, neonate, children): ").strip().lower()
        if dosing_strategy not in ['standard', 'neonate', 'children']:
            print("Invalid dosing strategy. Exiting program.")
            return

        patient_weight = None
        if dosing_strategy in ['neonate', 'children']:
            patient_weight = float(input("Enter the weight of the child in kg: ").strip())

        regimen_builder(treatments_to_use, dosing_strategy, patient_weight)
    else:
        print("Exiting program.")

if __name__ == "__main__":
    main()





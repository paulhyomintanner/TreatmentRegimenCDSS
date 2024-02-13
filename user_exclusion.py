from tinydb import TinyDB

# Primary filter for treatments. 
def filter_by_disease(treatments, diagnosis):
    diagnosis = diagnosis.lower()  
    return [treatment for treatment in treatments if treatment['disease'].lower() == diagnosis]  

#filtering by severity of the disease
def filter_by_severity(treatments, severity):
    severity = severity.lower()  
    return [treatment for treatment in treatments if treatment['severity'].lower() == severity]  

# filter treatments based on user exclusions
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
                break  

        if not exclude_treatment:
            filtered_treatments.append(treatment)

    return filtered_treatments

# Function to rank treatments based on the preferred CPG. Enters the rank attribute dictionary and finds the corresponding ranking based on theCPG. 
def rank_treatments(treatments, preferred_cpg):
    return sorted(treatments, key=lambda x: x['rank'][0][preferred_cpg])

def exclude_treatments(treatments):
    excluded_ids = input("Enter treatment IDs to exclude (comma-separated): ").strip().split(',')
    excluded_ids = [id.strip().upper() for id in excluded_ids]  
    return [treatment for treatment in treatments if treatment['treatment_id'] not in excluded_ids]

def print_treatments(treatments, diagnosis):
    print(f"\nTreatments for {diagnosis}:")
    for treatment in treatments:
        print(f"ID: {treatment['treatment_id']}, Treatment: {treatment}")


def process_treatments(treatments, disease, severity, exclusions, preferred_cpg):
    treatments = filter_by_disease(treatments, disease)
    treatments = filter_by_exclusions(treatments, exclusions)
    treatments = filter_by_severity(treatments, severity)
    ranked_treatments = rank_treatments(treatments, preferred_cpg)
    print_treatments(ranked_treatments, disease)
    print("\nYou can now exclude treatments from the ranked list.")
    updated_treatments = exclude_treatments(ranked_treatments)
    ranked_treatments = rank_treatments(updated_treatments, preferred_cpg)
    print_treatments(ranked_treatments, disease)
    return ranked_treatments

def main():
    db = TinyDB('treatment_db.json')
    all_treatments = db.all()

    preferred_cpg = input("Preferred CPG (WHO/NICE): ").strip()
    exclusions = input("Exclusions (comma-separated): ").strip().split(',')
    primary_diagnosis = input("Primary diagnosis: ").strip()
    severity = input("Primary diagnosis severity (low/high): ").strip()
    has_comorbidity = input("Comorbidity? (yes/no): ").strip().lower() == "yes"

    process_treatments(all_treatments, primary_diagnosis, severity, exclusions, preferred_cpg)

    if has_comorbidity:
        comorbidity = input("Comorbidity name: ").strip()
        comorbidity_severity = input("Comorbidity severity (low/high): ").strip()
        process_treatments(all_treatments, comorbidity, comorbidity_severity, exclusions, preferred_cpg)


if __name__ == "__main__":
    main()

"""Simplifying the script by using the tinydb to deal with the treatment data. Streamlined the functions """
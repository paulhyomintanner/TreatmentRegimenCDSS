from tinydb import TinyDB, Query

# function dealing with the primary disease
def filter_by_disease(treatments, diagnosis):
    diagnosis = diagnosis.lower()  
    return [treatment for treatment in treatments if treatment['disease'].lower() == diagnosis]  # Normalized the input and list to lowercase
#filtering by severity of the disease
def filter_by_severity(treatments, severity):
    severity = severity.lower()  
    return [treatment for treatment in treatments if treatment['severity'].lower() == severity]  

# filter treatments based on user exclusions
def filter_by_exclusions(treatments, exclusions):
    # Normalize exclusions to lowercase and strip whitespace
    exclusions = [exclusion.strip().lower() for exclusion in exclusions if exclusion.strip()]

    filtered_treatments = []
    for treatment in treatments:
        medication_list = treatment['medication']
        exclude_treatment = False

        for med in medication_list:
            med_exclusions = [ex.lower() for ex in med.get('exclusion', [])]  # Normalize medication exclusions to lowercase
            if any(exclusion in med_exclusions for exclusion in exclusions):
                exclude_treatment = True
                break  # Break the loop if any exclusion matches

        if not exclude_treatment:
            filtered_treatments.append(treatment)

    return filtered_treatments

# Function to rank treatments based on the preferred CPG. Enters the rank attribute dictionary and finds the corresponding ranking based on theCPG. 
def rank_treatments(treatments, preferred_cpg):
    return sorted(treatments, key=lambda x: x['rank'][0][preferred_cpg])

# Function to print treatments
def print_treatments(treatments, diagnosis):
    print(f"\nTreatments for {diagnosis}:")
    for treatment in treatments:
        print(treatment)

# Main function to orchestrate the system
def main():
    # Open the database and retrieve all treatments once
    db = TinyDB('treatment_db.json')
    all_treatments = db.all()

    # Get user inputs
    preferred_cpg = input("Preferred CPG (WHO/NICE): ").strip() #have to input the CPG you want to use (it wil change the ranking system)
    exclusions = input("Exclusions (comma-separated): ").strip().split(',') #one input for all exclusions (presuming 1 patient)
    primary_diagnosis = input("Primary diagnosis: ").strip() #maybe need to change to disease1 and comorbidty to disease2...
    severity = input("Primary diagnosis severity (low/high): ").strip() #could theoretically be anything, but for now it's low or high
    has_comorbidity = input("Comorbidity? (yes/no): ").strip().lower() == "yes"
    comorbidity = None
    comorbidity_severity = None
    #add comorbidity if neeeded at the same time. 
    if has_comorbidity:
        comorbidity = input("Comorbidity name: ").strip()
        comorbidity_severity = input("Comorbidity severity (low/high): ").strip()

    # Filter and process treatments for primary diagnosis and comorbidity if present in the input.
    # Added printing to validate that the list is actually functioning as intended. 
    primary_diagnosis_treatments = filter_by_disease(all_treatments, primary_diagnosis)
    print(f"After filter_by_disease: {primary_diagnosis_treatments}")
    primary_diagnosis_treatments = filter_by_exclusions(primary_diagnosis_treatments, exclusions)
    print(f"After filter_by_exclusions: {primary_diagnosis_treatments}")
    primary_diagnosis_treatments = filter_by_severity(primary_diagnosis_treatments, severity)
    print(f"After filter_by_severity: {primary_diagnosis_treatments}")
    ranked_primary_treatments = rank_treatments(primary_diagnosis_treatments, preferred_cpg)
    print_treatments(ranked_primary_treatments, primary_diagnosis)

    if has_comorbidity:
        comorbidity_treatments = filter_by_disease(all_treatments, comorbidity)
        print(f"After filter_by_disease: {comorbidity_treatments}")
        comorbidity_treatments = filter_by_exclusions(comorbidity_treatments, exclusions)
        print(f"After filter_by_exclusions: {comorbidity_treatments}")
        comorbidity_treatments = filter_by_severity(comorbidity_treatments, comorbidity_severity)
        print(f"After filter_by_severity: {comorbidity_treatments}")
        ranked_comorbidity_treatments = rank_treatments(comorbidity_treatments, preferred_cpg)
        print_treatments(ranked_comorbidity_treatments, comorbidity)

if __name__ == "__main__":
    main()

""" this was creted to validate the lists, and trouble shooting, but it is not being used. I had issues passing the list, and then just made a new list instead """
from tinydb import TinyDB
db = TinyDB('new_db.json')
all_treatments = db.all()

def filter_by_disease(treatments, diagnosis):
    return [treatment for treatment in treatments 
            if treatment['indication'].lower() == diagnosis.lower()]

def filter_by_severity(treatments, severity):
    return [treatment for treatment in treatments for eligibility in treatment['eligibility'] 
            if eligibility['severity'].lower() == severity.lower()]

def filter_by_exclusions(treatments, exclusions):
    exclusions = [exclusion.strip().lower() for exclusion in exclusions if exclusion.strip()]
    return [treatment for treatment in treatments 
            if not any(any(exclusion in eligibility.get('exclusion', []) 
                           for exclusion in exclusions) for eligibility in treatment['eligibility'])]


"""def rank_treatments(treatments, preferred_cpg):
    return sorted(treatments, key=lambda x: x['rank'][0][preferred_cpg])"""

def rank_treatments(treatments, preferred_cpg):
    return sorted(treatments, key=lambda x: x['guideline'][preferred_cpg][0]['rank'])


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


def main():
    diseases = []
    treatments_by_disease = {}
    rejected_treatments = []  
    preferred_cpg = input("Preferred CPG (WHO/BNF): ").strip()
    exclusions = input("Exclusions e.g allergy (comma-separated): ").strip().split(',')

    while True:
        disease = input("Add diagnosis (name): ").strip()
        severity = input("Diagnosis severity (low/high): ").strip()
        diseases.append({'name': disease, 'severity': severity})

        add_extra_disease = input("Add another disease? (yes/no): ").strip().lower()
        if add_extra_disease != "yes":
            break

    while True:
        for disease_info in diseases:
            treatments_for_disease = filter_by_disease(all_treatments, disease_info['name'])
            treatments_for_severity = filter_by_severity(treatments_for_disease, disease_info['severity'])
            treatments_excluding_exclusions = filter_by_exclusions(treatments_for_severity, exclusions)
            ranked_treatments = [treatment for treatment in rank_treatments(treatments_excluding_exclusions, preferred_cpg) if treatment not in rejected_treatments]

            treatments_by_disease[disease_info['name']] = ranked_treatments

            if not ranked_treatments:
                print(f"No treatments found for {disease_info['name']} after applying exclusions and rejections.")
                return  

        recommended_treatments = rules(treatments_by_disease)
        for disease, treatment in recommended_treatments.items():
            print(f"Recommended treatment for {disease}: {treatment}")

        user_input = input("Do you accept the recommended treatment? (yes/no): ").strip().lower()
        if user_input == 'yes':
            break  
        else:
            rejected_treatment_ids = input("Enter treatment IDs you want to reject (separated by commas): ").strip().split(',')
            for rejected_treatment_id in rejected_treatment_ids:
                rejected_treatment_id = rejected_treatment_id.strip()  
                for treatments in treatments_by_disease.values():
                    for treatment in treatments:
                        if treatment['treatment_id'] == rejected_treatment_id:
                            rejected_treatments.append(treatment)
                            break

    if user_input == 'yes':
        print("You have accepted the following treatment plan:")
        for disease, treatments in recommended_treatments.items():
            if treatments:  
                print(f"{disease} - Confirmed treatment: {treatments}")
            else:
                print(f"No treatments available for {disease} after applying exclusions and rejections.")


if __name__ == "__main__":
    main()
"""Same process, just with new data structure for ranking and for the dosing strategies. """



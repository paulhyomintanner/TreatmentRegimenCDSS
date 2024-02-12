
def rank_treatments(treatments, preferred_cpg):
    treatments.sort(key=lambda x: x['rank'][0][preferred_cpg])
    return treatments

from tinydb import TinyDB, Query

def filter_by_disease(diagnosis):
    db = TinyDB('treatment_db.json')
    Treatment = Query()
    treatments = db.search(Treatment.disease.test(lambda x: x.lower() == diagnosis.lower()))
    return treatments

def filter_by_severity(treatments, severity):
    treatments[:] = [treatment for treatment in treatments if treatment['severity'].lower() == severity.lower()]
    return treatments

def filter_by_exclusions(treatments, exclusions):
    exclusions = [exclusion.strip().lower() for exclusion in exclusions if exclusion.strip()] 
    treatments[:] = [treatment for treatment in treatments 
                     if not any(exclusion in [excl.lower() for excl in medication.get('exclusion', [])]  
                                for medication in treatment['medication'] 
                                for exclusion in exclusions)]
    return treatments


def main():
    preferred_cpg = input("Preferred CPG (WHO/NICE): ").strip()
    exclusions = input("Exclusions (comma-separated): ").strip().split(',')
    primary_diagnosis = input("Primary diagnosis: ").strip()
    severity = input("Primary diagnosis severity (low/high): ").strip()
    has_comorbidity = input("Comorbidity? (yes/no): ").strip().lower() == "yes"
    comorbidity = None
    comorbidity_severity = None

    if has_comorbidity:
        comorbidity = input("Comorbidity name: ").strip()
        comorbidity_severity = input("Comorbidity severity (low/high): ").strip()

    treatments = filter_by_disease(primary_diagnosis)
    filter_by_exclusions(treatments, exclusions)
    filter_by_severity(treatments, severity)  # Add this line
    ranked_treatments = rank_treatments(treatments, preferred_cpg)
    print_treatments(ranked_treatments, primary_diagnosis)

    if has_comorbidity:
        comorbidity_treatments = filter_by_disease(comorbidity)
        filter_by_exclusions(comorbidity_treatments, exclusions)
        filter_by_severity(comorbidity_treatments, comorbidity_severity)  # Changed severity to comorbidity_severity
        ranked_comorbidity_treatments = rank_treatments(comorbidity_treatments, preferred_cpg)
        print_treatments(ranked_comorbidity_treatments, comorbidity)

def print_treatments(treatments, diagnosis):
    print(f"\nTreatments for {diagnosis}:")
    for treatment in treatments:
        print(treatment)

if __name__ == "__main__":
    main()

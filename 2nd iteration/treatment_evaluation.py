from rank_treatments import rank_treatments
from primary_filter import filter_by_disease
from eligibility import filter_by_exclusions, filter_by_severity

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
    filter_by_severity(treatments, severity) 
    ranked_treatments = rank_treatments(treatments, preferred_cpg)
    print_treatments(ranked_treatments, primary_diagnosis)

    if has_comorbidity:
        comorbidity_treatments = filter_by_disease(comorbidity)
        filter_by_exclusions(comorbidity_treatments, exclusions)
        filter_by_severity(comorbidity_treatments, comorbidity_severity) 
        ranked_comorbidity_treatments = rank_treatments(comorbidity_treatments, preferred_cpg)
        print_treatments(ranked_comorbidity_treatments, comorbidity)

def print_treatments(treatments, diagnosis):
    print(f"\nTreatments for {diagnosis}:")
    for treatment in treatments:
        print(treatment)

if __name__ == "__main__":
    main()


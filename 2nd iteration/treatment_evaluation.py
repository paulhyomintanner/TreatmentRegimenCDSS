from rank_treatments import rank_treatments
from exclude_treatments import exclude_treatments
from primary_filter import filter_treatments
#Deals with the input in the console
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

    # Handle the input for thediagnosis - unsure if I should just call the variable disease1 and disease2
    treatments = filter_treatments(primary_diagnosis, severity, exclusions)
    treatments = exclude_treatments(treatments)
    ranked_treatments = rank_treatments(treatments, preferred_cpg)
    print_treatments(ranked_treatments, primary_diagnosis)

    # Deal with the comorbidity if there is one inputted
    if has_comorbidity:
        comorbidity_treatments = filter_treatments(comorbidity, comorbidity_severity, exclusions)
        comorbidity_treatments = exclude_treatments(comorbidity_treatments)
        ranked_comorbidity_treatments = rank_treatments(comorbidity_treatments, preferred_cpg)
        print_treatments(ranked_comorbidity_treatments, comorbidity)

def print_treatments(treatments, diagnosis):
    print(f"\nTreatments for {diagnosis}:")
    for treatment in treatments:
        print(treatment)

if __name__ == "__main__":
    main()

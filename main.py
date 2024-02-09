from filters import TreatmentFilteringSystem
from ranking import rank_treatments
from treatments import Treatment
from user_exclusion import remove_treatments

def main():
#Added a bunch of fake treatments to test the system so  far.
    treatments = [
        Treatment(name="TreatmentA", indications=[("DiseaseA", "High")], drugs=["Drug1", "Drug2"], exclusions=["ConditionX"], eligible_for_all=False, rank=2),
        Treatment(name="TreatmentB", indications=[("DiseaseA", "High"), ("DiseaseB", "Moderate")], drugs=["Drug3"], exclusions=[], eligible_for_all=True, rank=1),
        Treatment(name="TreatmentC", indications=[("DiseaseB", "High")], drugs=["Drug4"], exclusions=["ConditionY"], eligible_for_all=False, rank=4),
        Treatment(name="TreatmentD", indications=[("DiseaseC", "Low"), ("DiseaseB", "Moderate")], drugs=["Drug5", "Drug6"], exclusions=["ConditionX", "ConditionZ"], eligible_for_all=False, rank=5),
        Treatment(name="TreatmentE", indications=[("DiseaseA", "Moderate"), ("DiseaseC", "High")], drugs=["Drug7"], exclusions=["ConditionY"], eligible_for_all=True, rank=3),
    ]

    filtering_system = TreatmentFilteringSystem(treatments)

    primary_disease = input("Enter the primary diagnosis name: ")
    primary_severity = input("Enter the primary diagnosis severity (High/Moderate/Low): ")

    primary_criteria = (primary_disease, primary_severity)

    has_comorbidity = input("Comorbidity (Yes or No): ").strip().lower()

    comorbidity_criteria = None
    if has_comorbidity == "yes":
        comorbidity = input("Input Comorbidity: ").strip()
        comorbidity_severity = input("Comorbidity Severity (High/Moderate/Low): ").strip()

        comorbidity_criteria = (comorbidity, comorbidity_severity)

    exclusion_criteria = input("Enter exclusion criteria (blank if no): ").strip()

    primary_filtered_treatments = filtering_system.apply_filters(primary_criteria, exclusion_criteria)
    ranked_primary_treatments = rank_treatments(primary_filtered_treatments)

    comorbidity_filtered_treatments = []

    if comorbidity_criteria:
        comorbidity_filtered_treatments = filtering_system.apply_filters(comorbidity_criteria, exclusion_criteria)
        ranked_comorbidity_treatments = rank_treatments(comorbidity_filtered_treatments)

    print("\nCandidate treatments for the primary diagnosis:")
    if ranked_primary_treatments:
        for treatment in ranked_primary_treatments:
            print(f"Name: {treatment.name}, Drugs: {', '.join(treatment.drugs)}")
    else:
        print("No treatments match the primary diagnosis criteria.")

    if has_comorbidity == "yes":
        print("\nCandidate treatments for the comorbidity:")
        if ranked_comorbidity_treatments:
            for treatment in ranked_comorbidity_treatments:
                print(f"Name: {treatment.name}, Drugs: {', '.join(treatment.drugs)}")
        else:
            print("No treatments match the comorbidity criteria.")

    print("\nCandidate treatments for the primary diagnosis:")
    if ranked_primary_treatments:
        for treatment in ranked_primary_treatments:
            print(f"Name: {treatment.name}, Drugs: {', '.join(treatment.drugs)}")
        ranked_primary_treatments = remove_treatments(ranked_primary_treatments)
        ranked_primary_treatments = rank_treatments(ranked_primary_treatments)
    else:
        print("No treatments match the primary diagnosis criteria.")

    if has_comorbidity == "yes":
        print("\nCandidate treatments for the comorbidity:")
        if ranked_comorbidity_treatments:
            for treatment in ranked_comorbidity_treatments:
                print(f"Name: {treatment.name}, Drugs: {', '.join(treatment.drugs)}")
            ranked_comorbidity_treatments = remove_treatments(ranked_comorbidity_treatments)
            ranked_comorbidity_treatments = rank_treatments(ranked_comorbidity_treatments)
        else:
            print("No treatments match the comorbidity criteria.")

    print("\nDiagnosis treatment candidate list for the primary diagnosis:")
    if ranked_primary_treatments:
        for treatment in ranked_primary_treatments:
            print(f"Name: {treatment.name}, Drugs: {', '.join(treatment.drugs)}")
    else:
        print("No treatments left for the primary diagnosis.")

    if has_comorbidity == "yes":
        print("\nComorbidity treatment candidate list:")
        if ranked_comorbidity_treatments:
            for treatment in ranked_comorbidity_treatments:
                print(f"Name: {treatment.name}, Drugs: {', '.join(treatment.drugs)}")
        else:
            print("No treatments left for the comorbidity.")

if __name__ == "__main__":
    main()

"""
    The main process to run the program. It takes the disease, severity of the disease and whether there are any exclusions
    for the diagnosis as an input. It'll also then ask the user if they have a comorbidity. If yes then the filtering process
    will then be run for the disease in the comorbidity. The treatments will then be ranked according to a pre-defined rank
    that is decided upon by a clincian. They will then be displayed to the user, who will then be able to exclude treatments.
    Once the user exclusion funtion is completed, the final list will be printed for the user to see. 

    Filter process: essentially filters all available treatments based on the the disease - severity input by the user. This 
    is the indication for the treatment, similar to howe a drug is indicated for a specific disease. 
    This could be changed to anythin theoretically, but as of now that is the main basis in which treatments are selected. 

    The ranking process is allows the system to prioritise certain treatments for the user, and identifies which ones are more 
    important than other ones. It also allows the treatments to be given priority even once the user has excluded them. 

    The user exclusion process lets the user have ultimnate control over the list of treatments. They could exclude them for any reason, 
    cultural, stock, no equipment (syringges), etc. This data is not available to the system, is in the context of the setting (low-income)
    there would be no way to allow for the system to automatically know the stock of teh supplies as there is no electronnic system
    keeping tabs on the stock. The cultural aspect is important, as perhaps in some countries a form of the medicaion may not be ideally used. 
"""
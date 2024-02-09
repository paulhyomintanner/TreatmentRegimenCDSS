from filters import TreatmentFilteringSystem
from ranking import rank_treatments
from treatments import Treatment
from user_exclusion import remove_treatments

def main():
    """
    The main function that executes the treatment regimen decision support system.
    It prompts the user for primary diagnosis, comorbidity, exclusion criteria,
    and filters the available treatments.
    It then ranks the treatments based on a pre-defined ranking. Then it displays the filtered treatments for the primary diagnosis
    and comorbidity (if applicable).
    Finally it allows the user to remove treatments from the list. Before printing the final list. 
    """
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

    # Criteria tuple for the primary diagnosis
    primary_criteria = (primary_disease, primary_severity)

    # Ask the user if they have a comorbidity
    has_comorbidity = input("Comorbidity (Yes or No): ").strip().lower()

    comorbidity_criteria = None
    if has_comorbidity == "yes":
        # If yes, prompt for comorbidity and its severity
        comorbidity = input("Input Comorbidity: ").strip()
        comorbidity_severity = input("Comorbidity Severity (High/Moderate/Low): ").strip()

        # Criteria tuple for the comorbidity
        comorbidity_criteria = (comorbidity, comorbidity_severity)

    # Prompt the user for any exclusion criteria (applies to both diagnosis and comorbidity)
    exclusion_criteria = input("Enter any exclusion criteria (leave blank if none): ").strip()

    # Apply filters for the primary diagnosis
    primary_filtered_treatments = filtering_system.apply_filters(primary_criteria, exclusion_criteria)
    ranked_primary_treatments = rank_treatments(primary_filtered_treatments)

    # Initialize an empty list for comorbidity filtered treatments
    comorbidity_filtered_treatments = []

    # If comorbidity is provided, apply filters for the comorbidity
    if comorbidity_criteria:
        comorbidity_filtered_treatments = filtering_system.apply_filters(comorbidity_criteria, exclusion_criteria)
        ranked_comorbidity_treatments = rank_treatments(comorbidity_filtered_treatments)

    # Display the filtered treatments for the primary diagnosis
    print("\nAvailable treatments for the primary diagnosis:")
    if ranked_primary_treatments:
        for treatment in ranked_primary_treatments:
            print(f"Name: {treatment.name}, Drugs: {', '.join(treatment.drugs)}")
    else:
        print("No available treatments match the primary diagnosis criteria.")

    # Display the filtered treatments for the comorbidity (if applicable)
    if has_comorbidity == "yes":
        print("\nAvailable treatments for the comorbidity:")
        if ranked_comorbidity_treatments:
            for treatment in ranked_comorbidity_treatments:
                print(f"Name: {treatment.name}, Drugs: {', '.join(treatment.drugs)}")
        else:
            print("No available treatments match the comorbidity criteria.")

    # Display the filtered treatments for the primary diagnosis
    print("\nAvailable treatments for the primary diagnosis:")
    if ranked_primary_treatments:
        for treatment in ranked_primary_treatments:
            print(f"Name: {treatment.name}, Drugs: {', '.join(treatment.drugs)}")
        # Allow the user to remove treatments
        ranked_primary_treatments = remove_treatments(ranked_primary_treatments)
        # Re-rank the treatments
        ranked_primary_treatments = rank_treatments(ranked_primary_treatments)
    else:
        print("No available treatments match the primary diagnosis criteria.")

    # Display the filtered treatments for the comorbidity (if applicable)
    if has_comorbidity == "yes":
        print("\nAvailable treatments for the comorbidity:")
        if ranked_comorbidity_treatments:
            for treatment in ranked_comorbidity_treatments:
                print(f"Name: {treatment.name}, Drugs: {', '.join(treatment.drugs)}")
            # Allow the user to remove treatments
            ranked_comorbidity_treatments = remove_treatments(ranked_comorbidity_treatments)
            # Re-rank the treatments
            ranked_comorbidity_treatments = rank_treatments(ranked_comorbidity_treatments)
        else:
            print("No available treatments match the comorbidity criteria.")

    # Display the final list of treatments for the primary diagnosis
    print("\nFinal list of treatments for the primary diagnosis:")
    if ranked_primary_treatments:
        for treatment in ranked_primary_treatments:
            print(f"Name: {treatment.name}, Drugs: {', '.join(treatment.drugs)}")
    else:
        print("No treatments left for the primary diagnosis.")

    # Display the final list of treatments for the comorbidity (if applicable)
    if has_comorbidity == "yes":
        print("\nFinal list of treatments for the comorbidity:")
        if ranked_comorbidity_treatments:
            for treatment in ranked_comorbidity_treatments:
                print(f"Name: {treatment.name}, Drugs: {', '.join(treatment.drugs)}")
        else:
            print("No treatments left for the comorbidity.")

if __name__ == "__main__":
    main()


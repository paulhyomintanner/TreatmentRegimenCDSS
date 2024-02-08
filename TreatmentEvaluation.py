from abc import ABC, abstractmethod

class TreatmentFilter(ABC):
    @abstractmethod
    def filter(self, treatments, criteria):
        pass

class IndicationFilter(TreatmentFilter):
    def filter(self, treatments, criteria):
        filtered_treatments = []
        for treatment in treatments:
            if treatment.is_eligible(*criteria):  # Unpack criteria tuple
                filtered_treatments.append(treatment)
        return filtered_treatments

class ExclusionFilter(TreatmentFilter):
    def filter(self, treatments, exclusion_criteria):
        if not exclusion_criteria:  # If no exclusion criteria is provided, return all treatments
            return treatments

        filtered_treatments = []
        for treatment in treatments:
            # Exclude treatments that have the matching exclusion
            if exclusion_criteria not in treatment.exclusions:
                filtered_treatments.append(treatment)
        return filtered_treatments

class Treatment:
    def __init__(self, name, indications, drugs=None, exclusions=None, eligible_for_all=True):
        self.name = name
        self.indications = indications  # List of tuples (disease, severity)
        self.drugs = drugs if drugs else []  # List of drugs
        self.exclusions = exclusions if exclusions else []
        self.eligible_for_all = eligible_for_all

    def add_drug(self, drug_name):
        # Adds a new drug to the treatment
        self.drugs.append(drug_name)

    def add_indication(self, disease, severity):
        # Adds a new disease-severity pair to the indications list
        self.indications.append((disease, severity))

    def is_eligible(self, disease, severity):
        # Check if this treatment is eligible for the given disease and severity
        for indication in self.indications:
            if indication == (disease, severity):
                return True
        return False

    def __repr__(self):
        # Representation modified to accommodate the new structure
        indications_str = ', '.join([f"({disease}, {severity})" for disease, severity in self.indications])
        return f"Treatment(name='{self.name}', drugs={self.drugs}, indications=[{indications_str}], exclusions={self.exclusions}, eligible_for_all={self.eligible_for_all})"

class TreatmentFilteringSystem:
    def __init__(self, treatments):
        self.treatments = treatments
        self.indication_filter = IndicationFilter()
        self.exclusion_filter = ExclusionFilter()

    def apply_filters(self, indication_criteria, exclusion_criteria=None):
        """
        Apply indication and exclusion filters to the treatments.

        :param indication_criteria: A tuple containing (disease, severity).
        :param exclusion_criteria: A string representing the exclusion criteria. Optional.
        :return: A list of Treatment objects that match the filters.
        """
        # First, filter treatments based on indication
        filtered_treatments = self.indication_filter.filter(self.treatments, indication_criteria)

        # If exclusion criteria is provided, further filter the treatments
        if exclusion_criteria:
            filtered_treatments = self.exclusion_filter.filter(filtered_treatments, exclusion_criteria)

        return filtered_treatments
    
# Define a list of Treatment instances as your treatment database
treatments = [
    Treatment(name="TreatmentA", indications=[("DiseaseA", "High")], drugs=["Drug1", "Drug2"], exclusions=["ConditionX"], eligible_for_all=False),
    Treatment(name="TreatmentB", indications=[("DiseaseA", "High"), ("DiseaseB", "Moderate")], drugs=["Drug3"], exclusions=[], eligible_for_all=True),
    Treatment(name="TreatmentC", indications=[("DiseaseB", "High")], drugs=["Drug4"], exclusions=["ConditionY"], eligible_for_all=False),
    Treatment(name="TreatmentD", indications=[("DiseaseC", "Low"), ("DiseaseB", "Moderate")], drugs=["Drug5", "Drug6"], exclusions=["ConditionX", "ConditionZ"], eligible_for_all=False),
    Treatment(name="TreatmentE", indications=[("DiseaseA", "Moderate"), ("DiseaseC", "High")], drugs=["Drug7"], exclusions=["ConditionY"], eligible_for_all=True),
]

def main():
    # Instantiate the TreatmentFilteringSystem with the list of treatments
    filtering_system = TreatmentFilteringSystem(treatments)

    # Prompt the user for primary diagnosis name and severity
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

    # Initialize an empty list for comorbidity filtered treatments
    comorbidity_filtered_treatments = []

    # If comorbidity is provided, apply filters for the comorbidity
    if comorbidity_criteria:
        comorbidity_filtered_treatments = filtering_system.apply_filters(comorbidity_criteria, exclusion_criteria)

    # Display the filtered treatments for the primary diagnosis
    print("\nAvailable treatments for the primary diagnosis:")
    if primary_filtered_treatments:
        for treatment in primary_filtered_treatments:
            print(treatment)
    else:
        print("No available treatments match the primary diagnosis criteria.")

    # Display the filtered treatments for the comorbidity (if applicable)
    if has_comorbidity == "yes":
        print("\nAvailable treatments for the comorbidity:")
        if comorbidity_filtered_treatments:
            for treatment in comorbidity_filtered_treatments:
                print(treatment)
        else:
            print("No available treatments match the comorbidity criteria.")


if __name__ == "__main__":
    main()

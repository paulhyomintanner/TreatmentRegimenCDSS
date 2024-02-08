from abc import ABC, abstractmethod

class TreatmentFilter(ABC):
    @abstractmethod
    def filter(self, treatments, criteria):
        pass
        """
        Method to filter treatments based on given criteria.
        
        Args:
            treatments: The list of treatments to be filtered.
            criteria: The criteria based on which the treatments will be filtered.
        """
class IndicationFilter(TreatmentFilter):
    def filter(self, treatments, criteria):
        """
        Filters the given treatments based on the provided criteria.

        Args:
            treatments (list): List of treatments to be filtered.
            criteria (tuple): Criteria used for filtering the treatments.

        Returns:
            list: Filtered list of treatments.
        """
        filtered_treatments = []
        for treatment in treatments:
            if treatment.is_eligible(*criteria): 
                filtered_treatments.append(treatment)
        return filtered_treatments
 
class ExclusionFilter(TreatmentFilter):
    def filter(self, treatments, exclusion_criteria):
        """
        Filters the given treatments based on the provided exclusion criteria.

        Args:
            treatments (list): A list of treatments to be filtered.
            exclusion_criteria (str): The exclusion criteria to be used for filtering.

        Returns:
            list: A list of treatments that do not have the matching exclusion criteria.
        """
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
        """
        Initializes a new instance of the class.

        Args:
            treatments (list): A list of treatments.

        Attributes:
            self.treatments (list): The list of treatments.
            self.indication_filter (IndicationFilter): An instance of the IndicationFilter class.
            self.exclusion_filter (ExclusionFilter): An instance of the ExclusionFilter class.
        """
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
        
        filtered_treatments = self.indication_filter.filter(self.treatments, indication_criteria)

        if exclusion_criteria:
            filtered_treatments = self.exclusion_filter.filter(filtered_treatments, exclusion_criteria)

        return filtered_treatments
    
treatments = [
    Treatment(name="TreatmentA", indications=[("DiseaseA", "High")], drugs=["Drug1", "Drug2"], exclusions=["ConditionX"], eligible_for_all=False),
    Treatment(name="TreatmentB", indications=[("DiseaseA", "High"), ("DiseaseB", "Moderate")], drugs=["Drug3"], exclusions=[], eligible_for_all=True),
    Treatment(name="TreatmentC", indications=[("DiseaseB", "High")], drugs=["Drug4"], exclusions=["ConditionY"], eligible_for_all=False),
    Treatment(name="TreatmentD", indications=[("DiseaseC", "Low"), ("DiseaseB", "Moderate")], drugs=["Drug5", "Drug6"], exclusions=["ConditionX", "ConditionZ"], eligible_for_all=False),
    Treatment(name="TreatmentE", indications=[("DiseaseA", "Moderate"), ("DiseaseC", "High")], drugs=["Drug7"], exclusions=["ConditionY"], eligible_for_all=True),
]

def main():
    """
    Function to handle the main logic of the treatment filtering system.
    """
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

    exclusion_criteria = input("Enter any exclusion criteria (leave blank if none): ").strip()

    primary_filtered_treatments = filtering_system.apply_filters(primary_criteria, exclusion_criteria)

    comorbidity_filtered_treatments = []

    if comorbidity_criteria:
        comorbidity_filtered_treatments = filtering_system.apply_filters(comorbidity_criteria, exclusion_criteria)

    print("\nAvailable treatments for the primary diagnosis:")
    if primary_filtered_treatments:
        for treatment in primary_filtered_treatments:
            print(treatment)
    else:
        print("No available treatments match the primary diagnosis criteria.")

    if has_comorbidity == "yes":
        print("\nAvailable treatments for the comorbidity:")
        if comorbidity_filtered_treatments:
            for treatment in comorbidity_filtered_treatments:
                print(treatment)
        else:
            print("No available treatments match the comorbidity criteria.")


if __name__ == "__main__":
    main()


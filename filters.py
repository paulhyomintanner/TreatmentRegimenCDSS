from abc import ABC, abstractmethod

class TreatmentFilter(ABC):
    @abstractmethod
    def filter(self, treatments, criteria):
        pass

class IndicationFilter(TreatmentFilter):
    def filter(self, treatments, criteria):
        filtered_treatments = []
        for treatment in treatments:
            if treatment.is_eligible(*criteria):
                filtered_treatments.append(treatment)
        return filtered_treatments

class ExclusionFilter(TreatmentFilter):
    def filter(self, treatments, exclusion_criteria):
        if not exclusion_criteria:
            return treatments

        filtered_treatments = []
        for treatment in treatments:
            if exclusion_criteria not in treatment.exclusions:
                filtered_treatments.append(treatment)
        return filtered_treatments

class TreatmentFilteringSystem:
    def __init__(self, treatments):
        self.treatments = treatments
        self.indication_filter = IndicationFilter()
        self.exclusion_filter = ExclusionFilter()

    def apply_filters(self, indication_criteria, exclusion_criteria=None):
        filtered_treatments = self.indication_filter.filter(self.treatments, indication_criteria)
        if exclusion_criteria:
            filtered_treatments = self.exclusion_filter.filter(filtered_treatments, exclusion_criteria)
        return filtered_treatments



#the filters module is the fist set of functions that are called to filter the treatments
#the indication filter filters based on teh severity-disease pair, then the exclusion filter deals with the exclusion criteria. Specific treatment selection.
#there is also teh need potentially for the postcoordination filter as well, as this would further allow for a more specific treatment selection.

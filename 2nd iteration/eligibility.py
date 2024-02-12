def filter_by_severity(treatments, severity): 
    treatments[:] = [treatment for treatment in treatments if treatment['severity'].lower() == severity.lower()]
    return treatments
# Filters the treatments based on the user inputted severity i.e. low or high

def filter_by_exclusions(treatments, exclusions):
    exclusions = [exclusion.strip().lower() for exclusion in exclusions if exclusion.strip()]  
    treatments[:] = [treatment for treatment in treatments 
                     if not any(exclusion in [excl.lower() for excl in medication.get('exclusion', [])]  
                                for medication in treatment['medication'] 
                                for exclusion in exclusions)]
    return treatments

  # Filters the treatments based on the user inputted exclusion i.e. conditionX or pregnancy etc.


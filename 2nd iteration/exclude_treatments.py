def exclude_treatments(treatments):
    # This function will need to consider patient-specific exclusions, as of now though it is not integrated yet. 
    patient_exclusions = []  
    filtered_treatments = []
    for treatment in treatments:
        if all(exclusion not in treatment['medication'][0]['exclusion'] for exclusion in patient_exclusions):
            filtered_treatments.append(treatment)
    return filtered_treatments

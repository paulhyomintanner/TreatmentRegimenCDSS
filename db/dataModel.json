

{
    "treatment_id": str,
    "disease": str,
    "description": str,  # description of the treatment
    "eligibility": [
        {
            "data_strategy": str, #strategy that is used for eligibility
            "severity": {str: str}, #severity scale : level of severity e.g. "severity": {"CURB65": "High"},
            "exclusion": [str], #exclusions/ contraindications e.g. pregnancy, allergy, asthma, etc 
            "patient_profile": {"age_range": {"min": int, "max": int}, "min_weight":  int}, #profile of patient that is eligible for the treatment
        }
    ],
    "rank": [
        {
            "WHO":  int, #the cpg/ guidance body priority of the treatment
            "BNF":  int
        }
    ],
    "medication": [
        {
            "drug": str,    #name of the drug
            "form": {"type": str,"divisible": bool}, #form of the drug and if it is divisible. e.g. "form": {"type": "liquid","divisible": True},. Needed for dosage calc. 
            "site": str,    #where the drug is administered e.g. mouth, vein
            "route": str,   #how the drug is administered e.g. intravenous, oral, etc
            "method": str,  #method of administration e.g. inject
            "dose_strategy": {
                "type": str, #how the dose is calculated e.g. bsa, weight, etc. This indicates what dose calculation if any to use. 
                "sequence":  1,
                "text": str, #text for the dose calculation
                "patientInstruction": str, #patient instruction for the dose
                "timing": {
                    "repeat": {
                        "frequency":  int,
                        "period":  int,
                        "periodUnit": str, #unit of the period e.g. day, week, month, year, etc
                        "code": {
                            "text": str #text for the period
                        }
                    }
                },
                "route": {
                    "text": str
                },
                "doseAndRate": [
                    {
                        "type": {
                            "text": str #type of dose, single dose per cycle, etc OR use as needed etc. 
                        },
                        "doseQuantity": {
                            "value":  int,
                            "unit": str, #unit of the dose e.g. mg, mg/kg, mg/m2 etc. 
                            "system": "http://unitsofmeasure.org",
                            "code": str #code for the unit of the dose e.g. mg, mg/kg, mg/m2 etc.
                        }
                    }
                ],
                "maxDosePerPeriod": {
                    "numerator": {
                        "value":  int,
                        "unit": str
                    },
                    "denominator": {
                        "value":  int,
                        "unit": str #unit of the period e.g. day, week, month, year, etc
                    }
                }
            }
        }
    ]
}

#Example below for a made up treatment. 

{
    "treatment_id": "E",
    "disease": "DiseaseA",
    "description": "Used in lymphoma treatment cases",
    "eligibility": [
        {
            "strategy": "Basic strategy",
            "severity": {"Random_Scale": "High"},
            "exclusion": ["allergy to cyclophosphamide"],
            "patient_profile": {"age_range": {"min": 1, "max": 100}, "min_weight":  1},
        }
    ],
    "rank": [
        {
            "WHO":  5,
            "BNF":  1
        }
    ],
    "medication": [
        {
            "drug": "drug5",
            "form": {"type": "liquid","divisible": True},
            "site": "vein",
            "route": "intravenous",
            "method": "inject",
            "dose_strategy": {
                "type": "BSA",
                "sequence":  1,
                "text": "Administer Cyclophosphamide  750 mg/m^2 IV on Day  1 of each  28-day cycle.",
                "additionalInstruction": [
                    {
                        "text": "Pre-hydration and post-hydration required."
                    }
                ],
                "patientInstruction": "Administered on the first day of a  28-day cycle. Ensure proper hydration before and after administration.",
                "timing": {
                    "repeat": {
                        "frequency":  1,
                        "period":  28,
                        "periodUnit": "d",
                        "code": {
                            "text": "Every  28 days"
                        }
                    }
                },
                "route": {
                    "text": "Intravenous"
                },
                "doseAndRate": [
                    {
                        "type": {
                            "text": "Single dose per cycle"
                        },
                        "doseQuantity": {
                            "value":  750,
                            "unit": "mg/m^2",
                            "system": "http://unitsofmeasure.org",
                            "code": "mg^m2"
                        }
                    }
                ],
                "maxDosePerPeriod": {
                    "numerator": {
                        "value":  1000,
                        "unit": "mg",
                        "system": "http://unitsofmeasure.org",
                        "code": "mg"
                    },
                    "denominator": {
                        "value":  28,
                        "unit": "day",
                        "system": "http://unitsofmeasure.org",
                        "code": "d"
                    }
                }
            }
        }
    ]
}
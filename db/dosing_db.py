from tinydb import TinyDB
from typing import List, Dict

dosing_db = TinyDB('dosing_db.json')

treatment_data = [
    {
        "treatment_id": "A",
        "disease": "DiseaseA",
        "description": "Used in pediatric bacterial infection cases",
        "eligibility": [
            {
                "severity": {"CURB-65": "High"},
                "exclusion": ["penicillin"],
                "patient_profile": {"age_range": {"min": 18, "max": 65}, "min_weight":  45}
            }
        ],
        "rank": [
            {
                "WHO":  1,
                "BNF":  5
            }
        ],
        "medication": [
            {
                "drug": "Drug1",
                "form": "oral suspension",
                "site": "mouth",
                "route": "oral",
                "method": "swallow",
                "dose_strategy": {
                    "calculation": "yes",
                    "sequence":  1,
                    "text": "Administer Amoxicillin  50 mg/kg/day in divided doses every  8 hours.",
                    "additionalInstruction": [
                        {
                            "text": "Take with food to reduce gastrointestinal discomfort."
                        }
                    ],
                    "patientInstruction": "Divide the total daily dose into three equal doses. Administer every  8 hours with meals.",
                    "timing": {
                        "repeat": {
                            "frequency":  4,
                            "period":  1,
                            "periodUnit": "d",
                            "code": {
                                "text": "Every  8 hours"
                            }
                        }
                    },
                    "route": {
                        "text": "Oral"
                    },
                    "doseAndRate": [
                        {
                            "type": {
                                "text": "Daily dose"
                            },
                            "doseQuantity": {
                                "value":  50,
                                "unit": "mg/kg",
                                "system": "http://unitsofmeasure.org",
                                "code": "mg/kg"
                            }
                        }
                    ],
                    "maxDosePerPeriod": {
                        "numerator": {
                            "value":  4000,
                            "unit": "mg",
                            "system": "http://unitsofmeasure.org",
                            "code": "mg"
                        },
                        "denominator": {
                            "value":  1,
                            "unit": "day",
                            "system": "http://unitsofmeasure.org",
                            "code": "d"
                        }
                    }
                }
            },
            {
                "drug": "drug2",
                "form": "oral suspension",
                "site": "mouth",
                "route": "oral",
                "method": "swallow",
                "dose_strategy": {
                    "calculation": "yes",
                    "sequence":  1,
                    "text": "Administer Amoxicillin  50 mg/kg/day in divided doses every  8 hours.",
                    "additionalInstruction": [
                        {
                            "text": "Take with food to reduce gastrointestinal discomfort."
                        }
                    ],
                    "patientInstruction": "Divide the total daily dose into three equal doses. Administer every  8 hours with meals.",
                    "timing": {
                        "repeat": {
                            "frequency":  3,
                            "period":  1,
                            "periodUnit": "d",
                            "code": {
                                "text": "Every  8 hours"
                            }
                        }
                    },
                    "route": {
                        "text": "Oral"
                    },
                    "doseAndRate": [
                        {
                            "type": {
                                "text": "Daily dose"
                            },
                            "doseQuantity": {
                                "value":  50,
                                "unit": "mg/kg",
                                "system": "http://unitsofmeasure.org",
                                "code": "mg/kg"
                            }
                        }
                    ],
                    "maxDosePerPeriod": {
                        "numerator": {
                            "value":  1500,
                            "unit": "mg",
                            "system": "http://unitsofmeasure.org",
                            "code": "mg"
                        },
                        "denominator": {
                            "value":  1,
                            "unit": "day",
                            "system": "http://unitsofmeasure.org",
                            "code": "d"
                        }
                    }
                }
            }
        ]
    },
    {
        "treatment_id": "B",
        "disease": "DiseaseA",
        "description": "bacterial infection treatment for adults",
        "eligibility": [
            {
                "severity": {"CURB-65": "Low"},
                "exclusion": ["allergy to cyclophosphamide"],
                "patient_profile": {"age_range": {"min": 18, "max": 65}, "min_weight":  50},
            }
        ],
        "rank": [
            {
                "WHO":  2,
                "BNF":  4
            }
        ],
        "medication": [
            {
                "drug": "Cyclophosphamide",
                "form": "IV injection",
                "site": "vein",
                "route": "intravenous",
                "method": "inject",
                "dose_strategy": {
                    "calculation": "yes",
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
                                "code": "mg/m2"
                            }
                        }
                    ],
                    "maxDosePerPeriod": {
                        "numerator": {
                            "value":  750,
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
    },
    {
        "treatment_id": "C",
        "disease": "DiseaseA",
        "description": "Used in lymphoma treatment cases",
        "eligibility": [
            {
                "severity": {"CURB-65": "High"},
                "exclusion": ["allergy to cyclophosphamide"],
                "patient_profile": {"age_range": {"min": 1, "max": 17}, "min_weight":  2},
            }
        ],
        "rank": [
            {
                "WHO":  3,
                "BNF":  3
            }
        ],
        "medication": [
            {
                "drug": "drug3",
                "form": "IV injection",
                "site": "vein",
                "route": "intravenous",
                "method": "inject",
                "dose_strategy": {
                    "calculation": "yes",
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
                                "code": "mg/m2"
                            }
                        }
                    ],
                    "maxDosePerPeriod": {
                        "numerator": {
                            "value":  750,
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
    },
    {
        "treatment_id": "D",
        "disease": "DiseaseA",
        "description": "Used in lymphoma treatment cases",
        "eligibility": [
            {
                "severity": {"CURB-65": "High"},
                "exclusion": ["allergy to cyclophosphamide"],
                "patient_profile": {"age_range": {"min": 1, "max": 17}, "min_weight":  5},
            }
        ],
        "rank": [
            {
                "WHO":  4,
                "BNF":  2
            }
        ],
        "medication": [
            {
                "drug": "drug4",
                "form": "IV injection",
                "site": "vein",
                "route": "intravenous",
                "method": "inject",
                "dose_strategy": {
                    "calculation": "yes",
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
                                "code": "mg/m2"
                            }
                        }
                    ],
                    "maxDosePerPeriod": {
                        "numerator": {
                            "value":  750,
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
    },
    {
        "treatment_id": "E",
        "disease": "DiseaseA",
        "description": "Used in lymphoma treatment cases",
        "eligibility": [
            {
                "severity": {"CURB-65": "High"},
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
                "form": "IV injection",
                "site": "vein",
                "route": "intravenous",
                "method": "inject",
                "dose_strategy": {
                    "calculation": "yes",
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
                                "code": "mg/m2"
                            }
                        }
                    ],
                    "maxDosePerPeriod": {
                        "numerator": {
                            "value":  750,
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
    },
    {
        "treatment_id": "F",
        "disease": "DiseaseB",
        "description": "Used in lymphoma treatment cases",
        "eligibility": [
            {
                "severity": {"Pain": "Low"},
                "exclusion": ["allergy to cyclophosphamide"],
                "patient_profile": {"age_range": {"min": 18, "max": 65}, "min_weight":  40},
            }
        ],
        "rank": [
            {
                "WHO":  1,
                "BNF":  5
            }
        ],
        "medication": [
            {
                "drug": "drug6",
                "form": "IV injection",
                "site": "vein",
                "route": "intravenous",
                "method": "inject",
                "dose_strategy": {
                    "calculation": "yes",
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
                                "code": "mg/m2"
                            }
                        }
                    ],
                    "maxDosePerPeriod": {
                        "numerator": {
                            "value":  750,
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
    },
    {
        "treatment_id": "G",
        "disease": "DiseaseB",
        "description": "Used in lymphoma treatment cases",
        "eligibility": [
            {
                "severity": {"Pain": "Low"},
                "exclusion": ["allergy to cyclophosphamide"],
                "patient_profile": {"age_range": {"min": 18, "max": 65}, "min_weight":  40},
            }
        ],
        "rank": [
            {
                "WHO":  2,
                "BNF":  4
            }
        ],
        "medication": [
            {
                "drug": "drug7",
                "form": "IV injection",
                "site": "vein",
                "route": "intravenous",
                "method": "inject",
                "dose_strategy": {
                    "calculation": "yes",
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
                                "code": "mg/m2"
                            }
                        }
                    ],
                    "maxDosePerPeriod": {
                        "numerator": {
                            "value":  750,
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
    },
    {
        "treatment_id": "H",
        "disease": "DiseaseB",
        "description": "Used in lymphoma treatment cases",
        "eligibility": [
            {
                "severity": {"Pain": "Low"},
                "exclusion": ["allergy to cyclophosphamide"],
                "patient_profile": {"age_range": {"min": 1, "max": 65}, "min_weight":  10},
            }
        ],
        "rank": [
            {
                "WHO":  3,
                "BNF":  3
            }
        ],
        "medication": [
            {
                "drug": "drug8",
                "form": "IV injection",
                "site": "vein",
                "route": "intravenous",
                "method": "inject",
                "dose_strategy": {
                    "calculation": "yes",
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
                                "code": "mg/m2"
                            }
                        }
                    ],
                    "maxDosePerPeriod": {
                        "numerator": {
                            "value":  750,
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
    },
    {
        "treatment_id": "I",
        "disease": "drug9",
        "description": "Used in lymphoma treatment cases",
        "eligibility": [
            {
                "severity": {"Pain": "High"},
                "exclusion": ["allergy to cyclophosphamide"],
                "patient_profile": {"age_range": {"min": 1, "max": 65}, "min_weight":  10},
            }
        ],
        "rank": [
            {
                "WHO":  4,
                "BNF":  2
            }
        ],
        "medication": [
            {
                "drug": "Cyclophosphamide",
                "form": "IV injection",
                "site": "vein",
                "route": "intravenous",
                "method": "inject",
                "dose_strategy": {
                    "calculation": "yes",
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
                                "code": "mg/m2"
                            }
                        }
                    ],
                    "maxDosePerPeriod": {
                        "numerator": {
                            "value":  750,
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
    },
    {
        "treatment_id": "J",
        "disease": "DiseaseB",
        "description": "Used in lymphoma treatment cases",
        "eligibility": [
            {
                "severity": {"Pain": "High"},
                "exclusion": ["allergy to cyclophosphamide"],
                "patient_profile": {"age_range": {"min": 1, "max": 65}, "min_weight":  10},
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
                "drug": "Cyclophosphamide",
                "form": "IV injection",
                "site": "vein",
                "route": "intravenous",
                "method": "inject",
                "dose_strategy": {
                    "calculation": "yes",
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
                                "code": "mg/m2"
                            }
                        }
                    ],
                    "maxDosePerPeriod": {
                        "numerator": {
                            "value":  750,
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
]




dosing_db.insert_multiple(treatment_data)
dosing_db.close()



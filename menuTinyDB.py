from tinydb import TinyDB
from typing import List, Dict


menuTinyDB = TinyDB('menuTinyDB.json')

treatment_data = [
    {
        "treatment_id": "A",
        "disease": "DiseaseA",
        "description": "Used in pediatric bacterial infection cases",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"CURB65": "High"},
                "exclusion": ["penicillin", "dysphagia"],
                "patient_profile": {"age_range": {"min": 18, "max": 65}, "min_weight": 45}
            }
        ],
        "rank": [
            {
                "WHO": 1,
                "BNF": 5
            }
        ],
        "medication": [
            {
                "drug": "Drug1",
                "form": {"type": "tablet", "divisible": False},
                "site": "mouth",
                "route": "oral",
                "method": "swallow",
                "dose_strategy": [
                    {
                        "strategy": "weight",
                        "sequence": 1,
                        "text": "Administer Amoxicillin 50 mg/kg/day in divided doses every 8 hours.",
                        "additionalInstruction": [
                            {
                                "text": "Take with food to reduce gastrointestinal discomfort."
                            }
                        ],
                        "patientInstruction": "Divide the total daily dose into three equal doses. Administer every 8 hours with meals.",
                        "timing": {
                            "repeat": {
                                "frequency": 4,
                                "period": 1,
                                "periodUnit": "d",
                                "code": {
                                    "text": "Every 8 hours"
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
                                    "value": 50,
                                    "unit": "mg/kg",
                                    "system": "http://unitsofmeasure.org",
                                    "code": "mg/kg"
                                }
                            }
                        ],
                        "maxDosePerPeriod": {
                            "numerator": {
                                "value": 4000,
                                "unit": "mg",
                                "system": "http://unitsofmeasure.org",
                                "code": "mg"
                            },
                            "denominator": {
                                "value": 1,
                                "unit": "day",
                                "system": "http://unitsofmeasure.org",
                                "code": "d"
                            }
                        }
                    }
                ]
            },
            {
                "drug": "Drug2",
                "form": {"type": "liquid", "divisible": True},
                "site": "mouth",
                "route": "oral",
                "method": "swallow",
                "dose_strategy": [
                    {
                        "strategy": "bsa",
                        "sequence": 1,
                        "text": "Administer Amoxicillin 50 mg/kg/day in divided doses every 8 hours.",
                        "additionalInstruction": [
                            {
                                "text": "Take with food to reduce gastrointestinal discomfort."
                            }
                        ],
                        "patientInstruction": "Divide the total daily dose into three equal doses. Administer every 8 hours with meals.",
                        "timing": {
                            "repeat": {
                                "frequency": 3,
                                "period": 1,
                                "periodUnit": "d",
                                "code": {
                                    "text": "Every 8 hours"
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
                                    "value": 50,
                                    "unit": "mg/kg",
                                    "system": "http://unitsofmeasure.org",
                                    "code": "mg/kg"
                                }
                            }
                        ],
                        "maxDosePerPeriod": {
                            "numerator": {
                                "value": 1500,
                                "unit": "mg",
                                "system": "http://unitsofmeasure.org",
                                "code": "mg"
                            },
                            "denominator": {
                                "value": 1,
                                "unit": "day",
                                "system": "http://unitsofmeasure.org",
                                "code": "d"
                            }
                        }
                    }
                ]
            }
        ]
    },
    {
        "treatment_id": "B",
        "disease": "DiseaseA",
        "description": "bacterial infection treatment for adults",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"CURB65": "High"},
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
                "drug": "Drug3",
                "form": {"type": "IV","divisible":  True},
                "site": "vein",
                "route": "intravenous",
                "method": "inject",
                "dose_strategy": [
                    {
                        "strategy": "weight",
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
                ]
            }
        ]
    },
    {
        "treatment_id": "C",
        "disease": "DiseaseA",
        "description": "Used in lymphoma treatment cases",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"CURB65": "High"},
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
                "drug": "Drug4",
                "form": {"type": "tablet","divisible": True},
                "site": "vein",
                "route": "intravenous",
                "method": "inject",
                "dose_strategy": [
                    {
                        "strategy": "weight",
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
                ]
            }
        ]
    },
    {
        "treatment_id": "D",
        "disease": "DiseaseA",
        "description": "Used in lymphoma treatment cases",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"CURB65": "Low"},
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
                "drug": "Drug5",
                "form": {"type": "tablet","divisible":  False},
                "site": "vein",
                "route": "intravenous",
                "method": "inject",
                "dose_strategy": [
                    {
                        "strategy": "weight",
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
                ]
            }
        ]
    },
    {
        "treatment_id": "E",
        "disease": "DiseaseA",
        "description": "Used in lymphoma treatment cases",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"CURB65": "High"},
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
                "drug": "Drug6",
                "form": {"type": "liquid","divisible": True},
                "site": "vein",
                "route": "intravenous",
                "method": "inject",
                "dose_strategy": [
                    {
                        "strategy": "bsa",
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
                ]
           }
        ]
    },
    {
        "treatment_id": "F",
        "disease": "DiseaseB",
        "description": "Used in lymphoma treatment cases",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Pain":"low"},
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
                "drug": "Drug7",
                "form": {"type": "tablet","divisible":  True},
                "site": "vein",
                "route": "intravenous",
                "method": "inject",
                "dose_strategy": [
                    {
                        "strategy": "weight",
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
                ]
            }
        ]    
    },
    {
        "treatment_id": "G",
        "disease": "DiseaseB",
        "description": "Used in lymphoma treatment cases",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Pain":"low"},
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
                "drug": "Drug8",
                "form": {"type": "tablet","divisible":  True},
                "site": "vein",
                "route": "intravenous",
                "method": "inject",
                "dose_strategy": [
                    {
                        "strategy": "bsa",
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
                ]
            }
        ]
    },
    {
        "treatment_id": "H",
        "disease": "DiseaseB",
        "description": "Used in lymphoma treatment cases",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Pain":"High"},
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
                "drug": "Drug9",
                "form": {"type": "tablet","divisible":  False},
                "site": "vein",
                "route": "intravenous",
                "method": "inject",
                "dose_strategy": [
                    {
                        "strategy": "bsa",
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
                ]
            }
        ]
    },
    {
        "treatment_id": "I",
        "disease": "DiseaseC",
        "description": "Used in lymphoma treatment cases",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Pain":"low"},
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
                "drug": "Drug10",
                "form": {"type": "tablet","divisible":  False},
                "site": "vein",
                "route": "intravenous",
                "method": "inject",
                "dose_strategy": [
                    {
                        "strategy": "bsa",
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
                ]
            }
        ]
    },
    {
        "treatment_id": "J",
        "disease": "DiseaseB",
        "description": "Used in lymphoma treatment cases",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Pain":"low"},
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
                "drug": "Drug11",
                "form": {"type": "tablet","divisible": True},
                "site": "vein",
                "route": "intravenous",
                "method": "inject",
                "dose_strategy": [
                    {
                        "strategy": "bsa",
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
                                "value":  70000,
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
                ]
            }
        ]
    },
    {
        "treatment_id": "K",
        "disease": "DiseaseD",
        "description": "bacterial infection treatment for adults",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"CURB65": "High"},
                "exclusion": ["allergy to cyclophosphamide"],
                "patient_profile": {"age_range": {"min": 18, "max": 65}, "min_weight": 50}
            }
        ],
        "rank": [
            {"WHO": 6, "BNF": 6}
        ],
        "medication": [
            {
                "drug": "Drug3",
                "form": {"type": "IV", "divisible": True},
                "site": "vein",
                "route": "intravenous",
                "method": "inject",
                "dose_strategy": [
                    {
                        "strategy": "weight",
                        "sequence": 1,
                        "text": "Administer Cyclophosphamide 750 mg/m^2 IV on Day 1 of each 28-day cycle.",
                        "additionalInstruction": [
                            {"text": "Pre-hydration and post-hydration required."}
                        ],
                        "patientInstruction": "Administered on the first day of a 28-day cycle. Ensure proper hydration before and after administration.",
                        "timing": {
                            "repeat": {
                                "frequency": 1,
                                "period": 28,
                                "periodUnit": "d",
                                "code": {"text": "Every 28 days"}
                            }
                        },
                        "doseAndRate": [
                            {
                                "type": {"text": "Single dose per cycle"},
                                "doseQuantity": {
                                    "value": 750,
                                    "unit": "mg/m^2",
                                    "system": "http://unitsofmeasure.org",
                                    "code": "mg/m2"
                                }
                            }
                        ],
                        "maxDosePerPeriod": {
                            "numerator": {
                                "value": 1500, 
                                "unit": "mg",
                                "system": "http://unitsofmeasure.org",
                                "code": "mg"
                            },
                            "denominator": {
                                "value": 1,
                                "unit": "cycle",
                                "system": "http://unitsofmeasure.org",
                                "code": "cycle"
                            }
                        }
                    },
                    {
                        "strategy": "loading dose",
                        "sequence": 2,
                        "text": "Administer an initial loading dose followed by maintenance doses as per the therapeutic requirement.",
                        "additionalInstruction": [
                            {"text": "Assess renal function before adjusting maintenance doses."}
                        ],
                        "patientInstruction": "The initial dose is higher to quickly reach therapeutic levels.",
                        "timing": {
                            "repeat": {
                                "frequency": 1,
                                "period": 1,
                                "periodUnit": "d",
                                "code": {"text": "As needed based on therapeutic monitoring"}
                            }
                        },
                        "doseAndRate": [
                            {
                                "type": {"text": "Initial loading dose"},
                                "doseQuantity": {
                                    "value": 1000, 
                                    "unit": "mg",
                                    "system": "http://unitsofmeasure.org",
                                    "code": "mg"
                                }
                            }
                        ],
                        "maxDosePerPeriod": {
                            "numerator": {
                                "value": 2000, 
                                "unit": "mg",
                                "system": "http://unitsofmeasure.org",
                                "code": "mg"
                            },
                            "denominator": {
                                "value": 1,
                                "unit": "day",
                                "system": "http://unitsofmeasure.org",
                                "code": "d"
                            }
                        }
                    }                  
                ]
            }
        ]
    }
]

menuTinyDB.insert_multiple(treatment_data)
menuTinyDB.close()



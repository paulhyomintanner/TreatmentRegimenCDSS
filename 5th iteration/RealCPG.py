from tinydb import TinyDB
from typing import List, Dict


menuTinyDB = TinyDB('RealCPG.json')

treatment_data = [
    {
        "treatment_id": "A",
        "disease": "Acute Otitis Media",
        "description": "Used in pediatric bacterial infection cases",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Seriousness": "Low"},
                "exclusion": ["Penicillin allergy", "Dysphagia"],
                "patient_profile": {"age_range": {"min": 6, "max": 12}, "min_weight": 1}
            }
        ],
        "rank": [
            {
                "GHANA-STG": 1,
                "BNF": 5
            }
        ],
        "medication": [
            {
                "drug": "Paracetamol",
                "form": {"type": "tablet", "divisible": True},
                "site": "mouth",
                "route": "oral",
                "method": "swallow",
                "dose_strategy": [
                    {
                        "strategy": "Single Dose",
                        "sequence": 1,
                        "instruction": "250-500 mg of paracetamol 6-8 hourly to deal with pain",
                        "patientInstruction": "Divide the total daily dose into three equal doses. Administer every 8 hours with meals.",
                        "therapeuticDose": "250-500mg every 8 hours",
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
                        "doseAndRate": [
                            {
                                "doseQuantity": {
                                    "value": 500,
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
            },
            {
                "drug": "Amoxicillin",
                "form": {"type": "Tablet", "divisible": True},
                "site": "mouth",
                "route": "oral",
                "method": "swallow",
                "dose_strategy": [
                    {
                        "strategy": "Single Dose",
                        "sequence": 1,
                        "instruction": "250 mg 8 hourly for 10 days",
                        "patientInstruction": "Administer every 8 hours with meals.",
                        "therapeuticDose": "250mg every 8 hours",
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
                        "doseAndRate": [
                            {
                                "doseQuantity": {
                                    "value": 250,
                                    "unit": "mg",
                                    "system": "http://unitsofmeasure.org",
                                    "code": "mg"
                                }
                            }
                        ],
                        "maxDosePerPeriod": {
                            "numerator": {
                                "value": 1000,
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
        "disease": "Acute Otitis Media",
        "description": "Used in pediatric bacterial infection cases",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Seriousness": "High"},
                "exclusion": ["Penicillin allergy", "Dysphagia"],
                "patient_profile": {"age_range": {"min": 6, "max": 12}, "min_weight": 1}
            }
        ],
        "rank": [
            {
                "GHANA-STG": 1,
                "BNF": 5
            }
        ],
        "medication": [
            {
                "drug": "Paracetamol",
                "form": {"type": "tablet", "divisible": True},
                "site": "mouth",
                "route": "oral",
                "method": "swallow",
                "dose_strategy": [
                    {
                        "strategy": "Single Dose",
                        "sequence": 1,
                        "instruction": "250-500 mg of paracetamol 6-8 hourly to deal with pain",
                        "patientInstruction": "Divide the total daily dose into three equal doses. Administer every 8 hours with meals.",
                        "therapeuticDose": "250-500mg every 8 hours",
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
                        "doseAndRate": [
                            {
                                "doseQuantity": {
                                    "value": 500,
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
            },
            {
                "drug": "Amoxicillin + Clavulanic acid",
                "form": {"type": "Tablet", "divisible": True},
                "site": "mouth",
                "route": "oral",
                "method": "swallow (oral suspension)",
                "dose_strategy": [
                    {
                        "strategy": "Single Dose",
                        "sequence": 1,
                        "instruction": "5ml of 400/57mg suspension 12 hourly for 10 days",
                        "patientInstruction": "Administer every 12 hours with meals.",
                        "therapeuticDose": "5ml of 400/57mg",
                        "timing": {
                            "repeat": {
                                "frequency": 2,
                                "period": 1,
                                "periodUnit": "d",
                                "code": {
                                    "text": "Every 12 hours"
                                }
                            }
                        },
                        "doseAndRate": [
                            {
                                "doseQuantity": {
                                    "value": 400/57,
                                    "unit": "mg",
                                    "system": "http://unitsofmeasure.org",
                                    "code": "mg"
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
            }
        ]
    },
    {
        "treatment_id": "C",
        "disease": "Acute Otitis Media",
        "description": "Used in pediatric bacterial infection cases",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Seriousness": "Low"},
                "exclusion": ["Dysphagia"],
                "patient_profile": {"age_range": {"min": 2, "max": 8}, "min_weight": 1}
            }
        ],
        "rank": [
            {
                "GHANA-STG": 3,
                "BNF": 5
            }
        ],
        "medication": [
            {
                "drug": "Erythromycin",
                "form": {"type": "tablet", "divisible": True},
                "site": "mouth",
                "route": "oral",
                "method": "swallow",
                "dose_strategy": [
                    {
                        "strategy": "Single Dose",
                        "sequence": 1,
                        "instruction": "250 mg every 6 hours for 10 days",
                        "patientInstruction": "Divide the total daily dose into three equal doses. Administer every 8 hours with meals.",
                        "therapeuticDose": "250-500mg every 8 hours",
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
                        "doseAndRate": [
                            {
                                "doseQuantity": {
                                    "value": 250,
                                    "unit": "mg",
                                    "system": "http://unitsofmeasure.org",
                                    "code": "mg"
                                }
                            }
                        ],
                        "maxDosePerPeriod": {
                            "numerator": {
                                "value": 1000,
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
        "treatment_id": "D",
        "disease": "Acute Otitis Media",
        "description": "Used in pediatric bacterial infection cases",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Seriousness": "Low"},
                "exclusion": ["Dysphagia"],
                "patient_profile": {"age_range": {"min": 2, "max": 18}, "min_weight": 2}
            }
        ],
        "rank": [
            {
                "GHANA-STG": 4,
                "BNF": 5
            }
        ],
        "medication": [
            {
                "drug": "Azithromycin",
                "form": {"type": "tablet", "divisible": True},
                "site": "mouth",
                "route": "oral",
                "method": "swallow",
                "dose_strategy": [
                    {
                        "strategy": "weight",
                        "sequence": 1,
                        "instruction": "10 mg/kg once daily for 5 days",
                        "patientInstruction": "Administer one at meal.",
                        "therapeuticDose": "10mg/kg once daily for 5 days",
                        "timing": {
                            "repeat": {
                                "frequency": 1,
                                "period": 1,
                                "periodUnit": "d",
                                "code": {
                                    "text": "Once a day"
                                }
                            }
                        },
                        "doseAndRate": [
                            {
                                "doseQuantity": {
                                    "value": 10,
                                    "unit": "mg/kg",
                                    "system": "http://unitsofmeasure.org",
                                    "code": "mg/kg"
                                }
                            }
                        ],
                        "maxDosePerPeriod": {
                            "numerator": {
                                "value": 20,
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
        "treatment_id": "E",
        "disease": "Acute Otitis Media",
        "description": "Used in pediatric bacterial infection cases",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Seriousness": "High"},
                "exclusion": ["Dysphagia"],
                "patient_profile": {"age_range": {"min": 2, "max": 8}, "min_weight": 1}
            }
        ],
        "rank": [
            {
                "GHANA-STG": 3,
                "BNF": 5
            }
        ],
        "medication": [
            {
                "drug": "Erythromycin",
                "form": {"type": "tablet", "divisible": True},
                "site": "mouth",
                "route": "oral",
                "method": "swallow",
                "dose_strategy": [
                    {
                        "strategy": "Single Dose",
                        "sequence": 1,
                        "instruction": "250 mg every 6 hours for 10 days",
                        "patientInstruction": "Divide the total daily dose into three equal doses. Administer every 8 hours with meals.",
                        "therapeuticDose": "250-500mg every 8 hours",
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
                        "doseAndRate": [
                            {
                                "doseQuantity": {
                                    "value": 250,
                                    "unit": "mg",
                                    "system": "http://unitsofmeasure.org",
                                    "code": "mg"
                                }
                            }
                        ],
                        "maxDosePerPeriod": {
                            "numerator": {
                                "value": 1000,
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
        "treatment_id": "F",
        "disease": "Acute Otitis Media",
        "description": "Used in pediatric bacterial infection cases",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Seriousness": "High"},
                "exclusion": ["Dysphagia"],
                "patient_profile": {"age_range": {"min": 2, "max": 18}, "min_weight": 2}
            }
        ],
        "rank": [
            {
                "GHANA-STG": 4,
                "BNF": 5
            }
        ],
        "medication": [
            {
                "drug": "Azithromycin",
                "form": {"type": "tablet", "divisible": True},
                "site": "mouth",
                "route": "oral",
                "method": "swallow",
                "dose_strategy": [
                    {
                        "strategy": "weight",
                        "sequence": 1,
                        "instruction": "10 mg/kg once daily for 5 days",
                        "patientInstruction": "Administer one at meal.",
                        "therapeuticDose": "10mg/kg once daily for 5 days",
                        "timing": {
                            "repeat": {
                                "frequency": 1,
                                "period": 1,
                                "periodUnit": "d",
                                "code": {
                                    "text": "Once a day"
                                }
                            }
                        },
                        "doseAndRate": [
                            {
                                "doseQuantity": {
                                    "value": 10,
                                    "unit": "mg/kg",
                                    "system": "http://unitsofmeasure.org",
                                    "code": "mg/kg"
                                }
                            }
                        ],
                        "maxDosePerPeriod": {
                            "numerator": {
                                "value": 20,
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
        "treatment_id": "G",
        "disease": "Acute Otitis Media",
        "description": "Used in pediatric bacterial infection cases",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Seriousness": "Low"},
                "exclusion": ["Dysphagia"],
                "patient_profile": {"age_range": {"min": 2, "max": 8}, "min_weight": 1}
            }
        ],
        "rank": [
            {
                "GHANA-STG": 2,
                "BNF": 5
            }
        ],
        "medication": [
            {
                "drug": "Cefuroxime",
                "form": {"type": "tablet", "divisible": True},
                "site": "mouth",
                "route": "oral",
                "method": "swallow",
                "dose_strategy": [
                    {
                        "strategy": "Single Dose",
                        "sequence": 1,
                        "instruction": "125 mg 12 hourly for 5 days",
                        "patientInstruction": "Take twice a day",
                        "therapeuticDose": "125mg every 12 hours for 5 days",
                        "timing": {
                            "repeat": {
                                "frequency": 2,
                                "period": 1,
                                "periodUnit": "d",
                                "code": {
                                    "text": "Every 12 hours"
                                }
                            }
                        },
                        "doseAndRate": [
                            {
                                "doseQuantity": {
                                    "value": 125,
                                    "unit": "mg",
                                    "system": "http://unitsofmeasure.org",
                                    "code": "mg"
                                }
                            }
                        ],
                        "maxDosePerPeriod": {
                            "numerator": {
                                "value": 300,
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
        "treatment_id": "H",
        "disease": "Acute Otitis Media",
        "description": "Used in pediatric bacterial infection cases",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Seriousness": "High"},
                "exclusion": ["Dysphagia"],
                "patient_profile": {"age_range": {"min": 2, "max": 8}, "min_weight": 1}
            }
        ],
        "rank": [
            {
                "GHANA-STG": 2,
                "BNF": 5
            }
        ],
        "medication": [
            {
                "drug": "Cefuroxime",
                "form": {"type": "tablet", "divisible": True},
                "site": "mouth",
                "route": "oral",
                "method": "swallow",
                "dose_strategy": [
                    {
                        "strategy": "Single Dose",
                        "sequence": 1,
                        "instruction": "125 mg 12 hourly for 5 days",
                        "patientInstruction": "Take twice a day",
                        "therapeuticDose": "125mg every 12 hours for 5 days",
                        "timing": {
                            "repeat": {
                                "frequency": 2,
                                "period": 1,
                                "periodUnit": "d",
                                "code": {
                                    "text": "Every 12 hours"
                                }
                            }
                        },
                        "doseAndRate": [
                            {
                                "doseQuantity": {
                                    "value": 125,
                                    "unit": "mg",
                                    "system": "http://unitsofmeasure.org",
                                    "code": "mg"
                                }
                            }
                        ],
                        "maxDosePerPeriod": {
                            "numerator": {
                                "value": 300,
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



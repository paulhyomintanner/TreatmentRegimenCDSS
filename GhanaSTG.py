from tinydb import TinyDB
from typing import List, Dict

#source: https://www.moh.gov.gh/wp-content/uploads/2020/07/GhanaSTG-2017-1.pdf page 172-174 and p531
menuTinyDB = TinyDB('GhanaSTG.json')

treatment_data = [
    {
        "treatment_id": "A",
        "disease": "Acute Otitis Media",
        "description": "1st line for 6-12 year olds with low severity Acute Otitis Media",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Seriousness": "Low"},
                "exclusion": ["Penicillin Allergy", "Dysphagia"],
                "patient_profile": {"age_range": {"min": 6, "max": 12}, "min_weight": 1}
            }
        ],
        "rank": [
            {
                "GhanaSTG": 1,
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
                        "strategy": "single dose",
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
                        "strategy": "single dose",
                        "sequence": 2,
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
        "treatment_id": "A1",
        "disease": "Acute Otitis Media",
        "description": "1st line for 1-5 year olds with low severity Acute Otitis Media",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Seriousness": "Low"},
                "exclusion": ["Penicillin Allergy", "Dysphagia"],
                "patient_profile": {"age_range": {"min": 1, "max": 5}, "min_weight": 1}
            }
        ],
        "rank": [
            {
                "GhanaSTG": 1,
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
                        "strategy": "single dose",
                        "sequence": 1,
                        "instruction": "120-250 mg of paracetamol 6-8 hourly to deal with pain",
                        "patientInstruction": "Divide the total daily dose into three equal doses. Administer every 8 hours with meals.",
                        "therapeuticDose": "120-250 mg every 8 hours",
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
                                    "value": 120,
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
            },
            {
                "drug": "Amoxicillin",
                "form": {"type": "Tablet", "divisible": True},
                "site": "mouth",
                "route": "oral",
                "method": "swallow",
                "dose_strategy": [
                    {
                        "strategy": "single dose",
                        "sequence": 1,
                        "instruction": "125 mg 8 hourly for 10 days",
                        "patientInstruction": "Administer every 8 hours with meals.",
                        "therapeuticDose": "125mg every 8 hours",
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
                                    "value": 125,
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
        "description": "1st line treatment for 6-12 year olds with high severity Acute Otitis Media",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Seriousness": "High"},
                "exclusion": ["Penicillin Allergy", "Dysphagia"],
                "patient_profile": {"age_range": {"min": 6, "max": 12}, "min_weight": 1}
            }
        ],
        "rank": [
            {
                "GhanaSTG": 1,
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
                        "strategy": "single dose",
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
                        "strategy": "single dose",
                        "sequence": 2,
                        "instruction": "400/57mg (amox:clavulanic acid) suspension every 12 horus for 10 days",
                        "patientInstruction": "Administer every 12 hours with meals.",
                        "therapeuticDose": "Raito of 7:1  (400/57mg) Amoxicillin to Clavulanic acid",
                        "ratio": {
                            "amoxicillin": 7,
                            "clavulanic_acid": 1
                        },
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
                                    "value": 400,
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
        "treatment_id": "B1",
        "disease": "Acute Otitis Media",
        "description": "1st line treatment for 1-5 year olds with high severity Acute Otitis Media",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Seriousness": "High"},
                "exclusion": ["Penicillin Allergy", "Dysphagia"],
                "patient_profile": {"age_range": {"min": 1, "max": 5}, "min_weight": 1}
            }
        ],
        "rank": [
            {
                "GhanaSTG": 1,
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
                        "strategy": "single dose",
                        "sequence": 1,
                        "instruction": "120-250 mg of paracetamol 6-8 hourly to deal with pain",
                        "patientInstruction": "Divide the total daily dose into three equal doses. Administer every 8 hours with meals.",
                        "therapeuticDose": "120-250mg every 8 hours",
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
                                    "value": 120,
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
                        "strategy": "single dose",
                        "sequence": 2,
                        "instruction": "Ratio of 7:1 of 200/28.5mg (Amoxicillin to Clavulanic acid) suspension every 12 hours for 10 days",
                        "patientInstruction": "Administer every 12 hours with meals.",
                        "therapeuticDose": "200/28.5mg Amoxicillin to Clavulanic acid",
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
                                    "value": 200,
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
        "description": "Low severity AOM ages 3-8 with Penicillin Allergy",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Seriousness": "Low"},
                "exclusion": ["Dysphagia"],
                "patient_profile": {"age_range": {"min": 3, "max": 8}, "min_weight": 1}
            }
        ],
        "rank": [
            {
                "GhanaSTG": 3,
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
                        "strategy": "single dose",
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
        "treatment_id": "C1",
        "disease": "Acute Otitis Media",
        "description": "Low severity AOM ages 1-2 with Penicillin Allergy",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Seriousness": "Low"},
                "exclusion": ["Dysphagia"],
                "patient_profile": {"age_range": {"min": 1, "max": 2}, "min_weight": 1}
            }
        ],
        "rank": [
            {
                "GhanaSTG": 3,
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
                        "strategy": "single dose",
                        "sequence": 1,
                        "instruction": "125 mg every 6 hours for 10 days",
                        "patientInstruction": "Divide the total daily dose into three equal doses. Administer every 8 hours with meals.",
                        "therapeuticDose": "125mg every 8 hours",
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
                                    "value": 125,
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
        "description": "2nd line for children 1-18 with AOM Penicillin Allergy",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Seriousness": "Low"},
                "exclusion": ["Dysphagia"],
                "patient_profile": {"age_range": {"min": 1, "max": 18}, "min_weight": 2}
            }
        ],
        "rank": [
            {
                "GhanaSTG": 4,
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
                                "value": 200,
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
        "description": "Acute Otitis Media high severity ages 3-8",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Seriousness": "High"},
                "exclusion": ["Dysphagia"],
                "patient_profile": {"age_range": {"min": 3, "max": 8}, "min_weight": 1}
            }
        ],
        "rank": [
            {
                "GhanaSTG": 3,
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
                        "strategy": "single dose",
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
        "treatment_id": "E1",
        "disease": "Acute Otitis Media",
        "description": "Acute Otitis Media high severity ages 1-2",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Seriousness": "High"},
                "exclusion": ["Dysphagia"],
                "patient_profile": {"age_range": {"min": 1, "max": 2}, "min_weight": 1}
            }
        ],
        "rank": [
            {
                "GhanaSTG": 3,
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
                        "strategy": "single dose",
                        "sequence": 1,
                        "instruction": "120 mg every 6 hours for 10 days",
                        "patientInstruction": "Divide the total daily dose into three equal doses. Administer every 8 hours with meals.",
                        "therapeuticDose": "120 mg every 6 hours",
                        "timing": {
                            "repeat": {
                                "frequency": 4,
                                "period": 1,
                                "periodUnit": "d",
                                "code": {
                                    "text": "Every 6 hours"
                                }
                            }
                        },
                        "doseAndRate": [
                            {
                                "doseQuantity": {
                                    "value": 120,
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
        "description": "Acute Otitis Media high severity ages 1-18 with Penicillin Allergy",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Seriousness": "High"},
                "exclusion": ["Dysphagia"],
                "patient_profile": {"age_range": {"min": 1, "max": 18}, "min_weight": 2}
            }
        ],
        "rank": [
            {
                "GhanaSTG": 4,
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
        "description": "Acute Otitis Media low severity ages 1-18",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Seriousness": "Low"},
                "exclusion": ["Dysphagia", "Penicillin Allergy"],
                "patient_profile": {"age_range": {"min": 1, "max": 18}, "min_weight": 1}
            }
        ],
        "rank": [
            {
                "GhanaSTG": 2,
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
                        "strategy": "single dose",
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
        "description": "Acute Otitis Media high severity ages 1-18",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Seriousness": "High"},
                "exclusion": ["Dysphagia", "Penicillin Allergy"],
                "patient_profile": {"age_range": {"min": 1, "max": 18}, "min_weight": 1}
            }
        ],
        "rank": [
            {
                "GhanaSTG": 2,
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
                        "strategy": "single dose",
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
        "treatment_id": "I",
        "disease": "Acute Otitis Media",
        "description": "Acute Otitis Media low severity ages 19 above",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Seriousness": "Low"},
                "exclusion": ["Dysphagia", "Penicillin Allergy"],
                "patient_profile": {"age_range": {"min": 19, "max": 100}, "min_weight": 40}
            }
        ],
        "rank": [
            {
                "GhanaSTG": 1,
                "BNF": 5
            }
        ],
        "medication": [
            {
                "drug": "Amoxicillin",
                "form": {"type": "tablet", "divisible": True},
                "site": "mouth",
                "route": "oral",
                "method": "swallow",
                "dose_strategy": [
                    {
                        "strategy": "single dose",
                        "sequence": 1,
                        "instruction": "500 mg every 8 hours for 5 days",
                        "patientInstruction": "Take twice a day",
                        "therapeuticDose": "500mg",
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
            }
        ]
    },
    {
        "treatment_id": "J",
        "disease": "Acute Otitis Media",
        "description": "Acute Otitis Media high severity ages 19 and above",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Seriousness": "High"},
                "exclusion": ["Dysphagia", "Penicillin Allergy"],
                "patient_profile": {"age_range": {"min": 19, "max": 100}, "min_weight": 40}
            }
        ],
        "rank": [
            {
                "GhanaSTG": 1,
                "BNF": 5
            }
        ],
        "medication": [
            {
                "drug": "Amoxicillin + Clavulanic Acid",
                "form": {"type": "tablet", "divisible": True},
                "site": "mouth",
                "route": "oral",
                "method": "swallow",
                "dose_strategy": [
                    {
                        "strategy": "single dose",
                        "sequence": 1,
                        "instruction": "1000mg every 12 hours for 5 days",
                        "patientInstruction": "Take twice a day",
                        "therapeuticDose": "1000mg",
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
                                    "value": 1000,
                                    "unit": "mg",
                                    "system": "http://unitsofmeasure.org",
                                    "code": "mg"
                                }
                            }
                        ],
                        "maxDosePerPeriod": {
                            "numerator": {
                                "value": 3000,
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
        "treatment_id": "K",
        "disease": "Acute Otitis Media",
        "description": "High severity Acute Otitis Media for patients aged 9 and above with Penicillin Allergy",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Seriousness": "High"},
                "exclusion": ["Dysphagia"],
                "patient_profile": {"age_range": {"min": 9, "max": 100}, "min_weight": 40}
            }
        ],
        "rank": [
            {
                "GhanaSTG": 3,
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
                        "strategy": "single dose",
                        "sequence": 1,
                        "instruction": "250-500mg every 6 hours for 10 days",
                        "patientInstruction": "Take 4 a day",
                        "therapeuticDose": "500mg",
                        "timing": {
                            "repeat": {
                                "frequency": 4,
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
                                    "value": 500,
                                    "unit": "mg",
                                    "system": "http://unitsofmeasure.org",
                                    "code": "mg"
                                }
                            }
                        ],
                        "maxDosePerPeriod": {
                            "numerator": {
                                "value": 3000,
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
        "treatment_id": "K1",
        "disease": "Acute Otitis Media",
        "description": "Acute Otitis Media high severity 9 and above with Penicillin Allergy",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Seriousness": "Low"},
                "exclusion": ["Dysphagia"],
                "patient_profile": {"age_range": {"min": 9, "max": 100}, "min_weight": 40}
            }
        ],
        "rank": [
            {
                "GhanaSTG": 3,
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
                        "strategy": "single dose",
                        "sequence": 1,
                        "instruction": "250-500mg every 6 hours for 10 days",
                        "patientInstruction": "Take 4 a day",
                        "therapeuticDose": "500mg",
                        "timing": {
                            "repeat": {
                                "frequency": 4,
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
                                    "value": 500,
                                    "unit": "mg",
                                    "system": "http://unitsofmeasure.org",
                                    "code": "mg"
                                }
                            }
                        ],
                        "maxDosePerPeriod": {
                            "numerator": {
                                "value": 3000,
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
        "treatment_id": "L",
        "disease": "Acute Otitis Media",
        "description": "Acute Otitis Media low severity ages 19 and above with Penicillin Allergy",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Seriousness": "Low"},
                "exclusion": ["Dysphagia"],
                "patient_profile": {"age_range": {"min": 19, "max": 100}, "min_weight": 40}
            }
        ],
        "rank": [
            {
                "GhanaSTG": 4,
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
                        "strategy": "single dose",
                        "sequence": 1,
                        "instruction": "500mg 1 a day for 5 days",
                        "patientInstruction": "Take 1 a day",
                        "therapeuticDose": "500mg",
                        "timing": {
                            "repeat": {
                                "frequency": 3,
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
                                    "value": 500,
                                    "unit": "mg",
                                    "system": "http://unitsofmeasure.org",
                                    "code": "mg"
                                }
                            }
                        ],
                        "maxDosePerPeriod": {
                            "numerator": {
                                "value": 3000,
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
        "treatment_id": "L1",
        "disease": "Acute Otitis Media",
        "description": "Acute Otitis Media low severity ages 19 and above with Penicillin Allergy",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Seriousness": "High"},
                "exclusion": ["Dysphagia"],
                "patient_profile": {"age_range": {"min": 19, "max": 100}, "min_weight": 40}
            }
        ],
        "rank": [
            {
                "GhanaSTG": 4,
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
                        "strategy": "single dose",
                        "sequence": 1,
                        "instruction": "500mg 1 a day for 5 days",
                        "patientInstruction": "Take 1 a day",
                        "therapeuticDose": "500mg",
                        "timing": {
                            "repeat": {
                                "frequency": 3,
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
                                    "value": 500,
                                    "unit": "mg",
                                    "system": "http://unitsofmeasure.org",
                                    "code": "mg"
                                }
                            }
                        ],
                        "maxDosePerPeriod": {
                            "numerator": {
                                "value": 3000,
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
        "treatment_id": "M",
        "disease": "Acute Otitis Media",
        "description": "2nd line treatment for Acute Otitis Media low severity ages 19 and above",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Seriousness": "Low"},
                "exclusion": ["Dysphagia", "Penicillin Allergy"],
                "patient_profile": {"age_range": {"min": 19, "max": 100}, "min_weight": 40}
            }
        ],
        "rank": [
            {
                "GhanaSTG": 2,
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
                        "strategy": "single dose",
                        "sequence": 1,
                        "instruction": "250mg twice a day for 5 days",
                        "patientInstruction": "Take 2 a day",
                        "therapeuticDose": "250",
                        "timing": {
                            "repeat": {
                                "frequency": 3,
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
                                    "value": 250,
                                    "unit": "mg",
                                    "system": "http://unitsofmeasure.org",
                                    "code": "mg"
                                }
                            }
                        ],
                        "maxDosePerPeriod": {
                            "numerator": {
                                "value": 750,
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
        "treatment_id": "N",
        "disease": "Acute Otitis Media",
        "description": "2nd line treatment for Acute Otitis Media high severity ages 19 and above",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Seriousness": "High"},
                "exclusion": ["Dysphagia", "Penicillin Allergy"],
                "patient_profile": {"age_range": {"min": 19, "max": 100}, "min_weight": 40}
            }
        ],
        "rank": [
            {
                "GhanaSTG": 2,
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
                        "strategy": "single dose",
                        "sequence": 1,
                        "instruction": "250mg twice a day for 5 days",
                        "patientInstruction": "Take 2 a day",
                        "therapeuticDose": "250",
                        "timing": {
                            "repeat": {
                                "frequency": 3,
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
                                    "value": 250,
                                    "unit": "mg",
                                    "system": "http://unitsofmeasure.org",
                                    "code": "mg"
                                }
                            }
                        ],
                        "maxDosePerPeriod": {
                            "numerator": {
                                "value": 750,
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
        "treatment_id": "O",
        "disease": "Pneumonia",
        "description": "1st line treatment for less serious adult bacterial infection cases",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"CURB-65": "<2"},
                "exclusion": ["Dysphagia", "Penicillin Allergy"],
                "patient_profile": {"age_range": {"min": 18, "max": 100}, "min_weight": 10}
            }
        ],
        "rank": [
            {
                "GhanaSTG": 1,
                "BNF": 5
            }
        ],
        "medication": [
            {
                "drug": "Amoxicillin",
                "form": {"type": "tablet", "divisible": True},
                "site": "mouth",
                "route": "oral",
                "method": "swallow",
                "dose_strategy": [
                    {
                        "strategy": "single dose",
                        "sequence": 1,
                        "instruction": "1000mg 3 times a day for 7 days",
                        "patientInstruction": "Take 3 a day",
                        "therapeuticDose": "1000mg",
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
                        "doseAndRate": [
                            {
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
                                "value": 3000,
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
                "drug": "Azithromycin",
                "form": {"type": "tablet", "divisible": True},
                "site": "mouth",
                "route": "oral",
                "method": "swallow",
                "dose_strategy": [
                    {
                        "strategy": "single dose",
                        "sequence": 1,
                        "instruction": "500mg once a day for 7 days",
                        "patientInstruction": "Take 3 times a day",
                        "therapeuticDose": "500mg",
                        "timing": {
                            "repeat": {
                                "frequency": 1,
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
                                "value": 500,
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
        "treatment_id": "P",
        "disease": "Pneumonia",
        "description": "2nd line treatment for less serious adult bacterial infection cases",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"CURB-65": "<2"},
                "exclusion": ["Dysphagia", "Penicillin Allergy"],
                "patient_profile": {"age_range": {"min": 18, "max": 100}, "min_weight": 10}
            }
        ],
        "rank": [
            {
                "GhanaSTG": 2,
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
                        "strategy": "single dose",
                        "sequence": 1,
                        "instruction": "500mg 2 times a day for 7 days",
                        "patientInstruction": "Take 3 a day",
                        "therapeuticDose": "500mg",
                        "timing": {
                            "repeat": {
                                "frequency": 2,
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
        "treatment_id": "Q",
        "disease": "Pneumonia",
        "description": "1st line treatment for Penicillin Allergy",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"CURB-65": "<2"},
                "exclusion": ["Dysphagia"],
                "patient_profile": {"age_range": {"min": 19, "max": 100}, "min_weight": 10}
            }
        ],
        "rank": [
            {
                "GhanaSTG": 3,
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
                        "strategy": "single dose",
                        "sequence": 1,
                        "instruction": "500mg 4 times a day for 7 days",
                        "patientInstruction": "Take 3 a day",
                        "therapeuticDose": "500mg",
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
        "treatment_id": "R",
        "disease": "Pneumonia",
        "description": "2nd line treatment for Penicillin Allergy",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"CURB-65": "<2"},
                "exclusion": ["Dysphagia"],
                "patient_profile": {"age_range": {"min": 18, "max": 100}, "min_weight": 10}
            }
        ],
        "rank": [
            {
                "GhanaSTG": 4,
                "BNF": 5
            }
        ],
        "medication": [
            {
                "drug": "Doxycycline",
                "form": {"type": "tablet", "divisible": True},
                "site": "mouth",
                "route": "oral",
                "method": "swallow",
                "dose_strategy": [
                    {
                        "strategy": "single dose",
                        "sequence": 1,
                        "instruction": "100mg 2 times a day for 7 days",
                        "patientInstruction": "Take 2 a day",
                        "therapeuticDose": "100mg per dose",
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
                                    "value": 100,
                                    "unit": "mg",
                                    "system": "http://unitsofmeasure.org",
                                    "code": "mg"
                                }
                            }
                        ],
                        "maxDosePerPeriod": {
                            "numerator": {
                                "value": 200,
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
        "treatment_id": "S",
        "disease": "Pneumonia",
        "description": "1st line treatment for adult with serious Pneumonia",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"CURB-65": "≥2"},
                "exclusion": ["Penicillin Allergy", "Dysphagia"],
                "patient_profile": {"age_range": {"min": 18, "max": 100}, "min_weight": 10}
            }
        ],
        "rank": [
            {
                "GhanaSTG": 1,
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
                        "strategy": "single dose",
                        "sequence": 1,
                        "instruction": "500mg 3-4 times a day for 7 days for pain management",
                        "patientInstruction": "Take 2 a day",
                        "therapeuticDose": "500mg",
                        "timing": {
                            "repeat": {
                                "frequency": 3,
                                "period": 1,
                                "periodUnit": "d",
                                "code": {
                                    "text": "Every 6-8 hours"
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
                                "value": 3000,
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
                "form": {"type": "Liquid", "divisible": True},
                "site": "arm",
                "route": "IV",
                "method": "IV",
                "dose_strategy": [
                    {
                        "strategy": "single dose",
                        "sequence": 2,
                        "instruction": "1200mg every 8 hours for 7-10 days, change to oral when possible",
                        "patientInstruction": "Administer every 8 hours with meals.",
                        "therapeuticDose": "1200mg",
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
                        "doseAndRate": [
                            {
                                "doseQuantity": {
                                    "value": 1200,
                                    "unit": "mg",
                                    "system": "http://unitsofmeasure.org",
                                    "code": "mg"
                                }
                            }
                        ],
                        "maxDosePerPeriod": {
                            "numerator": {
                                "value": 5000,
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
                "drug": "Azithromycin",
                "form": {"type": "tablet", "divisible": True},
                "site": "oral",
                "route": "mouth",
                "method": "swallow",
                "dose_strategy": [
                    {
                        "strategy": "single dose",
                        "sequence": 1,
                        "instruction": "500mg once a day for 3 days",
                        "patientInstruction": "Administer every 12 hours with meals.",
                        "therapeuticDose": "500mg",
                        "timing": {
                            "repeat": {
                                "frequency": 1,
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
        "treatment_id": "T",
        "disease": "Pneumonia",
        "description": " 2nd line treatment for adult with serious Pneumonia who cannot swallow",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"CURB-65": "≥2"},
                "exclusion": ["Penicillin Allergy"],
                "patient_profile": {"age_range": {"min": 18, "max": 100}, "min_weight": 10}
            }
        ],
        "rank": [
            {
                "GhanaSTG": 2,
                "BNF": 5
            }
        ],
        "medication": [
            {
                "drug": "Paracetamol",
                "form": {"type": "suppository", "divisible": False},
                "site": "rectum",
                "route": "rectum",
                "method": "suppository",
                "dose_strategy": [
                    {
                        "strategy": "single dose",
                        "sequence": 1,
                        "instruction": "500mg 3-4 times a day for 7 days",
                        "patientInstruction": "Take 2 a day",
                        "therapeuticDose": "500mg",
                        "timing": {
                            "repeat": {
                                "frequency": 3,
                                "period": 1,
                                "periodUnit": "d",
                                "code": {
                                    "text": "Every 6-8 hours"
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
                                "value": 3000,
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
                "form": {"type": "Liquid", "divisible": True},
                "site": "arm",
                "route": "IV",
                "method": "IV",
                "dose_strategy": [
                    {
                        "strategy": "single dose",
                        "sequence": 1,
                        "instruction": "1200mg every 8 hours for 7-10 days",
                        "patientInstruction": "Administer every 12 hours with meals.",
                        "therapeuticDose": "1200mg",
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
                        "doseAndRate": [
                            {
                                "doseQuantity": {
                                    "value": 1200,
                                    "unit": "mg",
                                    "system": "http://unitsofmeasure.org",
                                    "code": "mg"
                                }
                            }
                        ],
                        "maxDosePerPeriod": {
                            "numerator": {
                                "value": 5000,
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
                "drug": "Azithromycin",
                "form": {"type": "Liquid", "divisible": True},
                "site": "arm",
                "route": "IV",
                "method": "IV",
                "dose_strategy": [
                    {
                        "strategy": "single dose",
                        "sequence": 1,
                        "instruction": "500mg once a day for 3-7 days, revert to oral Azithromycin when possible",
                        "patientInstruction": "Administer every 12 hours with meals.",
                        "therapeuticDose": "500mg",
                        "timing": {
                            "repeat": {
                                "frequency": 1,
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
        "treatment_id": "U",
        "disease": "Pneumonia",
        "description": " 1st line treatment for adult with serious Pneumonia and Penicillin Allergy",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"CURB-65": "≥2"},
                "exclusion": ["lactose intolerance"],
                "patient_profile": {"age_range": {"min": 18, "max": 100}, "min_weight": 10}
            }
        ],
        "rank": [
            {
                "GhanaSTG": 3,
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
                        "strategy": "single dose",
                        "sequence": 1,
                        "instruction": "500mg 3-4 times a day for 7 days",
                        "patientInstruction": "Take 2 a day",
                        "therapeuticDose": "500mg",
                        "timing": {
                            "repeat": {
                                "frequency": 3,
                                "period": 1,
                                "periodUnit": "d",
                                "code": {
                                    "text": "Every 6-8 hours"
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
                                "value": 3000,
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
                "drug": "Ceftriaxone",
                "form": {"type": "Liquid", "divisible": True},
                "site": "arm",
                "route": "IV",
                "method": "IV",
                "dose_strategy": [
                    {
                        "strategy": "single dose",
                        "sequence": 1,
                        "instruction": "2000mg once a day for 7-10 days",
                        "patientInstruction": "Administer every 12 hours with meals.",
                        "therapeuticDose": "2000mg",
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
                                    "value": 2000,
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
                "drug": "Azithromycin",
                "form": {"type": "Liquid", "divisible": True},
                "site": "arm",
                "route": "IV",
                "method": "IV",
                "dose_strategy": [
                    {
                        "strategy": "single dose",
                        "sequence": 1,
                        "instruction": "500mg once a day for 3-7 days, revert to oral Azithromycin when possible",
                        "patientInstruction": "Administer every 12 hours with meals.",
                        "therapeuticDose": "500mg",
                        "timing": {
                            "repeat": {
                                "frequency": 1,
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
        "treatment_id": "V",
        "disease": "Pneumonia",
        "description": "1st line treatment for less serious child bacterial infection cases",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"CURB-65": "<2"},
                "exclusion": ["Dysphagia", "Penicillin Allergy"],
                "patient_profile": {"age_range": {"min": 5, "max": 17}, "min_weight": 10}
            }
        ],
        "rank": [
            {
                "GhanaSTG": 1,
                "BNF": 5
            }
        ],
        "medication": [
            {
                "drug": "Amoxicillin",
                "form": {"type": "tablet", "divisible": True},
                "site": "mouth",
                "route": "oral",
                "method": "swallow",
                "dose_strategy": [
                    {
                        "strategy": "single dose",
                        "sequence": 1,
                        "instruction": "500mg 3 times a day for 7 days",
                        "patientInstruction": "Take 3 a day",
                        "therapeuticDose": "500mg",
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
                                "value": 3000,
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
                        "instruction": "10 mg/kg daily for 6 days",
                        "patientInstruction": "Take once a day",
                        "therapeuticDose": "10 mg/kg/day",
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
        "treatment_id": "W",
        "disease": "Pneumonia",
        "description": "1st line treatment for less serious young child bacterial infection cases",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"CURB-65": "<2"},
                "exclusion": ["Dysphagia", "Penicillin Allergy"],
                "patient_profile": {"age_range": {"min": 1, "max": 4}, "min_weight": 10}
            }
        ],
        "rank": [
            {
                "GhanaSTG": 1,
                "BNF": 5
            }
        ],
        "medication": [
            {
                "drug": "Amoxicillin",
                "form": {"type": "tablet", "divisible": True},
                "site": "mouth",
                "route": "oral",
                "method": "swallow",
                "dose_strategy": [
                    {
                        "strategy": "single dose",
                        "sequence": 1,
                        "instruction": "250mg 3 times a day for 7 days",
                        "patientInstruction": "Take 3 a day",
                        "therapeuticDose": "250mg",
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
                                "value": 3000,
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
                        "instruction": "10 mg/kg daily for 6 days",
                        "patientInstruction": "Take once a day",
                        "therapeuticDose": "10 mg/kg/day",
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
        "treatment_id": "X",
        "disease": "Pneumonia",
        "description": "2nd line treatment for less serious adult Pneumonia",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"CURB-65": "<2"},
                "exclusion": ["Dysphagia", "Penicillin Allergy"],
                "patient_profile": {"age_range": {"min": 1, "max": 12}, "min_weight": 10}
            }
        ],
        "rank": [
            {
                "GhanaSTG": 2,
                "BNF": 5
            }
        ],
        "medication": [
            {
                "drug": "Amoxicillin",
                "form": {"type": "tablet", "divisible": True},
                "site": "mouth",
                "route": "oral",
                "method": "swallow",
                "dose_strategy": [
                    {
                        "strategy": "weight",
                        "sequence": 1,
                        "instruction": "30mg/kg/day in two divided doses for 7 days",
                        "patientInstruction": "Take 2 times a day",
                        "therapeuticDose": "30mg/kg/day",
                        "timing": {
                            "repeat": {
                                "frequency": 2,
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
                                    "value": 30,
                                    "unit": "mg",
                                    "system": "http://unitsofmeasure.org",
                                    "code": "mg"
                                }
                            }
                        ],
                        "maxDosePerPeriod": {
                            "numerator": {
                                "value": 5000,
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
        "treatment_id": "Y",
        "disease": "Pneumonia",
        "description": "2nd line treatment for less serious adult bacterial infection cases",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"CURB-65": "<2"},
                "exclusion": ["Dysphagia", "Penicillin Allergy"],
                "patient_profile": {"age_range": {"min": 13, "max": 17}, "min_weight": 10}
            }
        ],
        "rank": [
            {
                "GhanaSTG": 1,
                "BNF": 5
            }
        ],
        "medication": [
            {
                "drug": "Amoxicillin",
                "form": {"type": "tablet", "divisible": True},
                "site": "mouth",
                "route": "oral",
                "method": "swallow",
                "dose_strategy": [
                    {
                        "strategy": "single dose",
                        "sequence": 1,
                        "instruction": "250-500mg every 12 hours for 7 days",
                        "patientInstruction": "Take 2 times a day",
                        "therapeuticDose": "250-500mg",
                        "timing": {
                            "repeat": {
                                "frequency": 2,
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
        "treatment_id": "Z",
        "disease": "Pneumonia",
        "description": "1st line treatment for Penicillin Allergy low severity",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"CURB-65": "<2"},
                "exclusion": ["Dysphagia"],
                "patient_profile": {"age_range": {"min": 2, "max": 8}, "min_weight": 10}
            }
        ],
        "rank": [
            {
                "GhanaSTG": 3,
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
                        "strategy": "single dose",
                        "sequence": 1,
                        "instruction": "250mg 4 times a day for 7 days",
                        "patientInstruction": "Take 3 a day",
                        "therapeuticDose": "250mg",
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
    },
    {
        "treatment_id": "AA",
        "disease": "Pneumonia",
        "description": "1st line treatment for child with Penicillin Allergy low severity",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"CURB-65": "<2"},
                "exclusion": ["Dysphagia"],
                "patient_profile": {"age_range": {"min": 9, "max": 17}, "min_weight": 10}
            }
        ],
        "rank": [
            {
                "GhanaSTG": 3,
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
                        "strategy": "single dose",
                        "sequence": 1,
                        "instruction": "500mg 4 times a day for 7 days",
                        "patientInstruction": "Take 3 a day",
                        "therapeuticDose": "500mg",
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
            }
        ]
    },
    {
        "treatment_id": "AB",
        "disease": "Pneumonia",
        "description": "2nd line treatment for Penicillin Allergy",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"CURB-65": "<2"},
                "exclusion": ["Dysphagia"],
                "patient_profile": {"age_range": {"min": 8, "max": 17}, "min_weight": 10}
            }
        ],
        "rank": [
            {
                "GhanaSTG": 4,
                "BNF": 5
            }
        ],
        "medication": [
            {
                "drug": "Doxycycline",
                "form": {"type": "tablet", "divisible": True},
                "site": "mouth",
                "route": "oral",
                "method": "swallow",
                "dose_strategy": [
                    {
                        "strategy": "single dose",
                        "sequence": 1,
                        "instruction": "100mg 2 times a day for 7 days",
                        "patientInstruction": "Take 2 a day",
                        "therapeuticDose": "100mg",
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
                                    "value": 100,
                                    "unit": "mg",
                                    "system": "http://unitsofmeasure.org",
                                    "code": "mg"
                                }
                            }
                        ],
                        "maxDosePerPeriod": {
                            "numerator": {
                                "value": 200,
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
        "treatment_id": "AC",
        "disease": "Pneumonia",
        "description": "1st line treatment for child with serious Pneumonia",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"CURB-65": "≥2"},
                "exclusion": ["Penicillin Allergy", "Dysphagia"],
                "patient_profile": {"age_range": {"min": 1, "max": 17}, "min_weight": 10}
            }
        ],
        "rank": [
            {
                "GhanaSTG": 1,
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
                        "strategy": "single dose",
                        "sequence": 1,
                        "instruction": "500mg 3-4 times a day for 7 days for pain management",
                        "patientInstruction": "Take 2 a day",
                        "therapeuticDose": "500mg",
                        "timing": {
                            "repeat": {
                                "frequency": 3,
                                "period": 1,
                                "periodUnit": "d",
                                "code": {
                                    "text": "Every 6-8 hours"
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
                                "value": 3000,
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
                "form": {"type": "Liquid", "divisible": True},
                "site": "arm",
                "route": "IV",
                "method": "IV",
                "dose_strategy": [
                    {
                        "strategy": "weight",
                        "sequence": 1,
                        "instruction": "30mg/kg  every 8 hours for 7 - days, change to oral when possible",
                        "patientInstruction": "Administer every 8 hours with meals.",
                        "therapeuticDose": "30mg/kg",
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
                        "doseAndRate": [
                            {
                                "doseQuantity": {
                                    "value": 30,
                                    "unit": "mg",
                                    "system": "http://unitsofmeasure.org",
                                    "code": "mg"
                                }
                            }
                        ],
                        "maxDosePerPeriod": {
                            "numerator": {
                                "value": 3600,
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
                "drug": "Azithromycin",
                "form": {"type": "tablet", "divisible": True},
                "site": "oral",
                "route": "mouth",
                "method": "swallow",
                "dose_strategy": [
                    {
                        "strategy": "weight",
                        "sequence": 1,
                        "instruction": "10mg/kg/day for 5 days",
                        "patientInstruction": "Administer every 12 hours with meals.",
                        "therapeuticDose": "10mg/kg/day",
                        "timing": {
                            "repeat": {
                                "frequency": 1,
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
                                    "value": 10,
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
        "treatment_id": "AD",
        "disease": "Pneumonia",
        "description": " 1st line of treatment and for patients with Penicillin Allergy",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"CURB-65": "≥2"},
                "exclusion": ["lactose intolerance"],
                "patient_profile": {"age_range": {"min": 1, "max": 17}, "min_weight": 10}
            }
        ],
        "rank": [
            {
                "GhanaSTG": 3,
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
                        "strategy": "single dose",
                        "sequence": 1,
                        "instruction": "250 -500mg 3-4 times a day for 7 days",
                        "patientInstruction": "Take 2 a day",
                        "therapeuticDose": "250-500mg",
                        "timing": {
                            "repeat": {
                                "frequency": 3,
                                "period": 1,
                                "periodUnit": "d",
                                "code": {
                                    "text": "Every 6-8 hours"
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
                                "value": 5000,
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
                "drug": "Ceftriaxone",
                "form": {"type": "Liquid", "divisible": True},
                "site": "arm",
                "route": "IV",
                "method": "IV",
                "dose_strategy": [
                    {
                        "strategy": "single dose",
                        "sequence": 1,
                        "instruction": "25mg/kg 2 times a day for 7-10 days",
                        "patientInstruction": "Administer every 12 hours",
                        "therapeuticDose": "25mg/kg",
                        "timing": {
                            "repeat": {
                                "frequency": 2,
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
                                    "value": 25,
                                    "unit": "mg",
                                    "system": "http://unitsofmeasure.org",
                                    "code": "mg"
                                }
                            }
                        ],
                        "maxDosePerPeriod": {
                            "numerator": {
                                "value": 5000,
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
                "drug": "Azithromycin",
                "form": {"type": "tablet", "divisible": True},
                "site": "oral",
                "route": "mouth",
                "method": "swallow",
                "dose_strategy": [
                    {
                        "strategy": "weight",
                        "sequence": 1,
                        "instruction": "10mg/kg/day for 5 days",
                        "patientInstruction": "Administer every 12 hours with meals.",
                        "therapeuticDose": "10mg/kg/day",
                        "timing": {
                            "repeat": {
                                "frequency": 1,
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
                                    "value": 10,
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
            }
        ]
    }
]



menuTinyDB.insert_multiple(treatment_data)
menuTinyDB.close()



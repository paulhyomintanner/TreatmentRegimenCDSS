from tinydb import TinyDB
from typing import List, Dict
#reference for the AOM: https://medicalguidelines.msf.org/en/viewport/CG/english/acute-otitis-media-aom-16689234.html

menuTinyDB = TinyDB('MSF_CPG.json')

treatment_data = [
    {
        "treatment_id": "MSF 1",
        "disease": "Acute Otitis Media",
        "description": "1st line for children with low severity Acute Otitis Media",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Seriousness": "Low severity"},
                "exclusion": ["Dysphagia", "Penicillin Allergy"],
                "patient_profile": {"age_range": {"min": 0, "max": 18}, "min_weight": 1}
            }
        ],
        "rank": [
            {
                "MSF": 1
            }
        ],
        "medication": [
            {
                "drug": "Amoxicillin",
                "form": {"type": "Tablet", "divisible": True},
                "site": "mouth (PO)",
                "route": "oral",
                "method": "swallow",
                "dose_strategy": [
                    {
                        "strategy": "weight",
                        "sequence": 1,
                        "instruction": "30mg/kg 3 times daily (max. 3 g daily)",
                        "patientInstruction": "Administer every 8 hours.",
                        "therapeuticDose": "30mg every 8 hours",
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
        "treatment_id": "MSF 2",
        "disease": "Acute Otitis Media",
        "description": "Treatment for children <40kg with high severity Acute Otitis Media",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Seriousness": "High severity"},
                "exclusion": ["Penicillin Allergy", "Dysphagia"],
                "patient_profile": {"age_range": {"min": 1, "max": 18}, "min_weight": 1}
            }
        ],
        "rank": [
            {
                "MSF": 1
            }
        ],
        "medication": [
            {
                "drug": "Amoxicillin and Clavulanic acid",
                "form": {"type": "Tablet","divisible": True},
                "site": "mouth",
                "route": "oral",
                "method": "swallow (oral suspension)",
                "dose_strategy": [
                    {
                        "strategy": "weight",
                        "sequence": 1,
                        "instruction": "Children <40 kg: 25mg/kg 2 times daily. Dose is for Amoxicillin",
                        "patientInstruction": "Take every 12 hours",
                        "therapeuticDose": "Ratio 8:1 of Amoxicillin (25mg/kg) to Clavulanic acid",
                        "ratio": {
                            "amoxicillin": 8,
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
                                    "value": 25,
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
    },
    {
        "treatment_id": "MSF 3",
        "disease": "Acute Otitis Media",
        "description": "1st line of treatment for adult with low severity Acute Otitis Media",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Seriousness": "Low severity"},
                "exclusion": ["Penicillin Allergy", "Dysphagia"],
                "patient_profile": {"age_range": {"min": 19, "max": 100}, "min_weight": 40}
            }
        ],
        "rank": [
            {
                "MSF": 1
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
                        "instruction": "Take 120-250 mg of paracetamol 6-8 hourly to deal with pain",
                        "patientInstruction": "Take every 8 hours",
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
                "drug": "Amoxicillin",
                "form": {"type": "Tablet", "divisible": True},
                "site": "mouth",
                "route": "oral",
                "method": "swallow (oral suspension)",
                "dose_strategy": [
                    {
                        "strategy": "single dose",
                        "sequence": 2,
                        "instruction": "Adults: 1000mg 3 times daily",
                        "patientInstruction": "Administer every 12 hours with meals.",
                        "therapeuticDose": "1000mg 3 times a day",
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
                                    "value": 1000,
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
        "treatment_id": "MSF 4",
        "disease": "Acute Otitis Media",
        "description": "2nd line of treatment for adult, or child over >40kg with Acute Otitis Media",
        "eligibility": [
            {
                "strategy": "Basic strategy",
                "severity": {"Seriousness": "High severity"},
                "exclusion": ["Dysphagia"],
                "patient_profile": {"age_range": {"min": 19, "max": 100}, "min_weight": 40}
            }
        ],
        "rank": [
            {
                "MSF": 1,
            }
        ],
        "medication": [
            {
                "drug": "Amoxicillin and Clavulanic acid",
                "form": {"type": "Tablet","divisible": True},
                "site": "mouth",
                "route": "oral",
                "method": "swallow (oral suspension)",
                "dose_strategy": [
                    {
                        "strategy": "single dose",
                        "sequence": 1,
                        "instruction": "Administer 1000mg(Amoxicillin)/125mg(Clavulanic acid) 2 times daily)",
                        "patientInstruction": "Take every 12 hours",
                        "therapeuticDose": "Ratio 8:1 of Amoxicillin (1000mg) to Clavulanic acid",
                        "ratio": {
                            "amoxicillin": 8,
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
                                    "value": 1000,
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
    }
]



menuTinyDB.insert_multiple(treatment_data)
menuTinyDB.close()



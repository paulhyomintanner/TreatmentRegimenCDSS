from tinydb import TinyDB

testing_db = TinyDB('testing_db.json')

treatment_data = [
    {
        "treatment_id": "A",
        "disease": "DiseaseA",
        "description": "used in X cases",
        "eligibility": [{ "severity":  "High", "exclusion": ["penicillin"]}],
        "rank": [{"WHO": 1, "BNF": 2}],
        "medication": [
            {
                "drug": "Ampicillin",
                "form": "tablet",
                "site": "mouth",
                "route": "oral",
                "method": "swallow",
                "dose_strategy": [
                    {
                        "standard": [
                            {
                                "dose_mg": 500,
                                "frequency_per_day": 8,
                                "max_dose_mg": 1000
                            }
                        ],
                        "weight": [
                            {
                                "mg/kg": 55,
                                "frequency_per_day": 12,
                                "max_dose_mg": 100
                            }
                        ]
                    }
                ]
            },
            {
                "drug": "drug123",
                "form": "tablet",
                "site": "mouth",
                "route": "oral",
                "method": "swallow",
                "dose_guideline": [
                    {
                        "standard": [
                            {
                                "dose_mg": 50,
                                "frequency_per_day": 8
                            }
                        ],
                        "weight": [
                            {
                                "mg/kg": 55,
                                "frequency_per_day": 12
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        "treatment_id": "B",  
        "disease": "DiseaseA",
        "description": "used in X cases",
        "form": "tablet",
        "site": "mouth",
        "route": "oral",
        "method": "swallow",
        "eligibility": [{ "severity":  "High", "exclusion": ["pregnant"]}],
        "rank": [{"WHO": 2, "BNF": 3}],
        "medication": [
            {
                "drug": "drug456",
                "form": "tablet",
                "site": "mouth",
                "route": "oral",
                "method": "swallow", 
                "dose_guideline": [
                    {
                        "standard": [
                            {
                                "dose_mg": 50,
                                "frequency_per_day": 2
                            }
                        ],
                        "weight": [
                            {
                                "mg/kg": 55,
                                "frequency_per_day": 12
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        "treatment_id": "C",
        "disease": "DiseaseA",
        "description": "used in X cases",
        "eligibility": [{ "severity":  "High", "exclusion": []}],
        "rank": [{"WHO":  3, "BNF":  2}],
        "medication": [
            {
                "drug": "drug789",
                "form": "tablet",
                "site": "mouth",
                "route": "oral",
                "method": "swallow",
                "dose_guideline": [
                    {
                        "standard": [
                            {
                                "dose_mg": 60,
                                "frequency_per_day": 8
                            }
                        ],
                        "weight": [
                            {
                                "mg/kg": 55,
                                "frequency_per_day": 12
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        "treatment_id": "D",
        "disease": "DiseaseB",
        "description": "used in X cases",
        "eligibility": [{ "severity":  "Low", "exclusion": []}],
        "rank": [{"WHO":  4, "BNF":  1}],
        "medication": [
            {
                "drug": "drug012",
                "form": "tablet",
                "site": "mouth",
                "route": "oral",
                "method": "swallow",
                "dose_guideline": [
                    {
                        "standard": [
                            {
                                "dose_mg": 70,
                                "frequency_per_day": 8
                            }
                        ],
                        "weight": [
                            {
                                "mg/kg": 55,
                                "frequency_per_day": 12
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        "treatment_id": "E",
        "disease": "DiseaseB",
        "description": "used in X cases",
        "eligibility": [{ "severity":  "Low", "exclusion": ["pregnant"]}],
        "rank": [{"WHO":  1, "BNF":  4}],
        "medication": [
            {
                "drug": "drug345",
                "form": "tablet",
                "site": "mouth",
                "route": "oral",
                "method": "swallow",
                "dose_guideline": [
                    {
                        "standard": [
                            {
                                "dose_mg": 80,
                                "frequency_per_day": 8
                            }
                        ],
                        "weight": [
                            {
                                "mg/kg": 55,
                                "frequency_per_day": 12
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        "treatment_id": "F",
        "disease": "DiseaseB",
        "description": "used in X cases",
        "eligibility": [{ "severity":  "Low", "exclusion": []}],
        "rank": [{"WHO":  3, "BNF":  2}],
        "medication": [
            {
                "drug": "drug678",
                "form": "tablet",
                "site": "mouth",
                "route": "oral",
                "method": "swallow",
                "dose_guideline": [
                    {
                        "standard": [
                            {
                                "dose_mg": 90,
                                "frequency_per_day": 8
                            }
                        ],
                        "weight": [
                            {
                                "mg/kg": 55,
                                "frequency_per_day": 12
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        "treatment_id": "G",
        "disease": "DiseaseB",
        "description": "used in X cases",
        "eligibility": [{ "severity":  "Low", "exclusion": []}],
        "rank": [{"WHO":  3, "BNF":  2}],
        "medication": [
            {
                "drug": "drug901",
                "form": "tablet",
                "site": "mouth",
                "route": "oral",
                "method": "swallow",
                "dose_guideline": [
                    {
                        "standard": [
                            {
                                "text": "Sodium nitroprusside for Hypertensive emergencies: Initially 0.5-1.5 micrograms/kg/minute, adjusted in steps of 500 nanograms/kg/minute every 5 minutes, usual dose 0.5-8 micrograms/kg/minute. Use lower doses if already receiving other antihypertensives. Stop if response unsatisfactory with max. dose in 10 minutes. A lower initial dose of 300 nanograms/kg/minute has been used.",
                                "timing": {
                                    "repeat": {
                                    "frequency": 12, 
                                    "period": 1,
                                    "periodUnit": "h"
                                    }
                                },
                                "route": {
                                    "coding": [
                                    {
                                        "system": "http://snomed.info/sct",
                                        "code": "47625008",
                                        "display": "Intravenous route"
                                    }
                                    ],
                                    "text": "BY INTRAVENOUS INFUSION"
                                },
                                "doseAndRate": [
                                    {
                                    "type": {
                                        "coding": [
                                        {
                                            "system": "http://terminology.hl7.org/CodeSystem/dose-rate-type",
                                            "code": "ordered",
                                            "display": "Ordered"
                                        }
                                        ],
                                        "text": "Initial dose"
                                    },
                                    "doseRange": {
                                        "low": {
                                        "value": 0.5,
                                        "unit": "micrograms/kg/minute",
                                        "system": "http://unitsofmeasure.org",
                                        "code": "ug/kg/min"
                                        },
                                        "high": {
                                        "value": 1.5,
                                        "unit": "micrograms/kg/minute",
                                        "system": "http://unitsofmeasure.org",
                                        "code": "ug/kg/min"
                                        }
                                    }
                                    },
                                    {
                                    "type": {
                                        "coding": [
                                        {
                                            "system": "http://terminology.hl7.org/CodeSystem/dose-rate-type",
                                            "code": "ordered",
                                            "display": "Adjustment step"
                                        }
                                        ],
                                        "text": "Adjustment step"
                                    },
                                    "doseQuantity": {
                                        "value": 0.5,
                                        "unit": "micrograms/kg/minute",
                                        "system": "http://unitsofmeasure.org",
                                        "code": "ug/kg/min"
                                    }
                                    },
                                    {
                                    "type": {
                                        "coding": [
                                        {
                                            "system": "http://terminology.hl7.org/CodeSystem/dose-rate-type",
                                            "code": "ordered",
                                            "display": "Usual dose"
                                        }
                                        ],
                                        "text": "Usual dose"
                                    },
                                    "doseRange": {
                                        "low": {
                                        "value": 0.5,
                                        "unit": "micrograms/kg/minute",
                                        "system": "http://unitsofmeasure.org",
                                        "code": "ug/kg/min"
                                        },
                                        "high": {
                                        "value": 8,
                                        "unit": "micrograms/kg/minute",
                                        "system": "http://unitsofmeasure.org",
                                        "code": "ug/kg/min"
                                        }
                                    }
                                    }
                                ],
                                "maxDosePerPeriod": {
                                    "numerator": {
                                    "value": 8,
                                    "unit": "micrograms/kg/minute",
                                    "system": "http://unitsofmeasure.org",
                                    "code": "ug/kg/min"
                                    },
                                    "denominator": {
                                    "value": 10,
                                    "unit": "minute",
                                    "system": "http://unitsofmeasure.org",
                                    "code": "min"
                                    }
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    }
]

testing_db.insert_multiple(treatment_data)
testing_db.close()

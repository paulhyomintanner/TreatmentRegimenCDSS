from tinydb import TinyDB

treatment_db = TinyDB('treatment_db.json')

treatment_data = [
    {
        "treatment_id": "A",
        "disease": "DiseaseA",
        "eligibility": [{ "severity":  "High", "exclusion": ["penicillin"]}],
        "rank": [{"WHO": 1, "NICE": 2}],
        "medication": [
            {
                "drug": "Ampicillin",
                "brand": ["brandU"],
                "dose_guideline": [
                    {
                        "standard": [
                            {
                                "dose_mg": 500,
                                "frequency_per_day": 8
                            }
                        ],
                        "neonate": [
                            {
                                "mg/kg": 30,
                                "frequency_per_day": 12
                            }
                        ],
                        "children": [
                            {
                                "mg/kg": 40,
                                "frequency_per_day": 8
                            }
                        ]
                    }
                ]
            },
            {
                "drug": "drug123",
                "brand": ["brandASD, brandX"],
                "dose_guideline": [
                    {
                        "standard": [
                            {
                                "dose_mg": 50,
                                "frequency_per_day": 8
                            }
                        ],
                        "neonate": [
                            {
                                "mg/kg": 30,
                                "frequency_per_day": 12
                            }
                        ],
                        "children": [
                            {
                                "mg/kg": 10,
                                "frequency_per_day": 8
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
        "eligibility": [{ "severity":  "High", "exclusion": ["pregnant"]}],
        "rank": [{"WHO": 2, "NICE": 3}],
        "medication": [
            {
                "drug": "drug456",
                "brand": ["brandU"],  
                "dose_guideline": [
                    {
                        "standard": [
                            {
                                "dose_mg": 50,
                                "frequency_per_day": 2
                            }
                        ],
                        "neonate": [
                            {
                                "mg/kg": 60,
                                "frequency_per_day": 6
                            }
                        ],
                        "children": [
                            {
                                "mg/kg": 40,
                                "frequency_per_day": 3
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
        "eligibility": [{ "severity":  "High", "exclusion": []}],
        "rank": [{"WHO":  3, "NICE":  2}],
        "medication": [
            {
                "drug": "drug789",
                "brand": ["brandU, brandV"],
                "dose_guideline": [
                    {
                        "standard": [
                            {
                                "dose_mg": 60,
                                "frequency_per_day": 8
                            }
                        ],
                        "neonate": [
                            {
                                "mg/kg": 35,
                                "frequency_per_day": 12
                            }
                        ],
                        "children": [
                            {
                                "mg/kg": 20,
                                "frequency_per_day": 8
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
        "eligibility": [{ "severity":  "Low", "exclusion": []}],
        "rank": [{"WHO":  4, "NICE":  1}],
        "medication": [
            {
                "drug": "drug012",
                "brand": ["brandU"],
                "dose_guideline": [
                    {
                        "standard": [
                            {
                                "dose_mg": 70,
                                "frequency_per_day": 8
                            }
                        ],
                        "neonate": [
                            {
                                "mg/kg": 40,
                                "frequency_per_day": 12
                            }
                        ],
                        "children": [
                            {
                                "mg/kg": 25,
                                "frequency_per_day": 8
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
        "eligibility": [{ "severity":  "Low", "exclusion": ["pregnant"]}],
        "rank": [{"WHO":  1, "NICE":  4}],
        "medication": [
            {
                "drug": "drug345",
                "brand": ["brandZ"],
                "dose_guideline": [
                    {
                        "standard": [
                            {
                                "dose_mg": 80,
                                "frequency_per_day": 8
                            }
                        ],
                        "neonate": [
                            {
                                "mg/kg": 45,
                                "frequency_per_day": 12
                            }
                        ],
                        "children": [
                            {
                                "mg/kg": 30,
                                "frequency_per_day": 8
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
        "eligibility": [{ "severity":  "Low", "exclusion": []}],
        "rank": [{"WHO":  3, "NICE":  2}],
        "medication": [
            {
                "drug": "drug678",
                "brand": ["brand123", "drug1235"],
                "dose_guideline": [
                    {
                        "standard": [
                            {
                                "dose_mg": 90,
                                "frequency_per_day": 8
                            }
                        ],
                        "neonate": [
                            {
                                "mg/kg": 50,
                                "frequency_per_day": 12
                            }
                        ],
                        "children": [
                            {
                                "mg/kg": 35,
                                "frequency_per_day": 8
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
        "eligibility": [{ "severity":  "Low", "exclusion": []}],
        "rank": [{"WHO":  3, "NICE":  2}],
        "medication": [
            {
                "drug": "drug901",
                "brand": ["amoxil", "drug1234"],
                "dose_guideline": [
                    {
                        "standard": [
                            {
                                "dose_mg": 100,
                                "frequency_per_day": 8
                            }
                        ],
                        "neonate": [
                            {
                                "mg/kg": 55,
                                "frequency_per_day": 12
                            }
                        ],
                        "children": [
                            {
                                "mg/kg": 40,
                                "frequency_per_day": 8
                            }
                        ]
                    }
                ]
            }
        ]
    }
]

treatment_db.insert_multiple(treatment_data)

print("All treatments in the database:")
for treatment in treatment_db:
    print(treatment)

treatment_db.close()

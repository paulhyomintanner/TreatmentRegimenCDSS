from tinydb import TinyDB

dosage_guide_db = TinyDB('dosage_guide.json')

treatment_dose = [
    {
        "treatment_id": "A",
        "disease": "DiseaseA",
        "severity": "High",
        "rank": [{"WHO": 1, "NICE": 2}],
        "medication": [
            {
                "drug": "Ampicillin",
                "brand": ["brandU"],
                "exclusion": ["penicillin"],
                "dose_guideline": [
                    {
                        "standard": [
                            {
                                "dose_mg": 500,
                                "frequency_hours": 8
                            }
                        ],
                        "neonate": [
                            {
                                "mg/kg": 30,
                                "frequency_hours": 12
                            }
                        ],
                        "children": [
                            {
                                "mg/kg": 40,
                                "frequency_hours": 8
                            }
                        ]
                    }
                ]
            },
            {
                "drug": "drug123",
                "brand": ["brandASD, brandX"],
                "exclusion": [],
                "dose_guideline": [
                    {
                        "standard": [
                            {
                                "dose_mg": 50,
                                "frequency_hours": 8
                            }
                        ],
                        "neonate": [
                            {
                                "mg/kg": 30,
                                "frequency_hours": 12
                            }
                        ],
                        "children": [
                            {
                                "mg/kg": 10,
                                "frequency_hours": 8
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
        "severity": "High",
        "rank": [{"WHO": 2, "NICE": 3}],
        "medication": [
            {
                "drug": "drug456",
                "brand": ["brandU"],
                "exclusion": ["pregnant"],  
                "dose_guideline": [
                    {
                        "standard": [
                            {
                                "dose_mg": 50,
                            }
                        ],
                        "neonate": [
                            {
                                "mg/kg": 60,
                            }
                        ],
                        "children": [
                            {
                                "mg/kg": 40,
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
        "severity": "High",
        "rank": [{"WHO":  3, "NICE":  2}],
        "medication": [
            {
                "drug": "drug789",
                "brand": ["brandU, brandV"],
                "exclusion": [],
                "dose_guideline": [
                    {
                        "standard": [
                            {
                                "dose_mg": 60,
                                "frequency_hours": 8
                            }
                        ],
                        "neonate": [
                            {
                                "mg/kg": 35,
                                "frequency_hours": 12
                            }
                        ],
                        "children": [
                            {
                                "mg/kg": 20,
                                "frequency_hours": 8
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
        "severity": "Low",
        "rank": [{"WHO":  4, "NICE":  1}],
        "medication": [
            {
                "drug": "drug012",
                "brand": ["brandU"],
                "exclusion": [],
                "dose_guideline": [
                    {
                        "standard": [
                            {
                                "dose_mg": 70,
                                "frequency_hours": 8
                            }
                        ],
                        "neonate": [
                            {
                                "mg/kg": 40,
                                "frequency_hours": 12
                            }
                        ],
                        "children": [
                            {
                                "mg/kg": 25,
                                "frequency_hours": 8
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
        "severity": "Low",
        "rank": [{"WHO":  1, "NICE":  4}],
        "medication": [
            {
                "drug": "drug345",
                "brand": ["brandZ"],
                "exclusion": ["pregnant"],
                "dose_guideline": [
                    {
                        "standard": [
                            {
                                "dose_mg": 80,
                                "frequency_hours": 8
                            }
                        ],
                        "neonate": [
                            {
                                "mg/kg": 45,
                                "frequency_hours": 12
                            }
                        ],
                        "children": [
                            {
                                "mg/kg": 30,
                                "frequency_hours": 8
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
        "severity": "Low",
        "rank": [{"WHO":  3, "NICE":  2}],
        "medication": [
            {
                "drug": "drug678",
                "brand": ["brand123", "drug1235"],
                "exclusion": [],
                "dose_guideline": [
                    {
                        "standard": [
                            {
                                "dose_mg": 90,
                                "frequency_hours": 8
                            }
                        ],
                        "neonate": [
                            {
                                "mg/kg": 50,
                                "frequency_hours": 12
                            }
                        ],
                        "children": [
                            {
                                "mg/kg": 35,
                                "frequency_hours": 8
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
        "severity": "Low",
        "rank": [{"WHO":  3, "NICE":  2}],
        "medication": [
            {
                "name": "drug901",
                "brand": ["amoxil", "drug1234"],
                "exclusion": [],
                "dose_guideline": [
                    {
                        "standard": [
                            {
                                "dose_mg": 100,
                                "frequency_hours": 8
                            }
                        ],
                        "neonate": [
                            {
                                "mg/kg": 55,
                                "frequency_hours": 12
                            }
                        ],
                        "children": [
                            {
                                "mg/kg": 40,
                                "frequency_hours": 8
                            }
                        ]
                    }
                ]
            }
        ]
    }
]

dosage_guide_db.insert_multiple(treatment_dose)

print("All treatments in the database:")
for treatment_dose in dosage_guide_db.all():
    print(treatment_dose)

dosage_guide_db.close()

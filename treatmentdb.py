from tinydb import TinyDB, Query

treatment_db = TinyDB('treatment_db.json')

treatment_data = [
    {
        "treatment_id": "A",
        "disease": "DiseaseA",
        "severity": "High",
        "rank": [{"WHO": 1, "NICE": 4}],
        "medication": [
            {
                "name": "Drug1",
                "exclusion": ["ConditionX"],
            },
            {
                "name": "Drug2",
                "exclusion": [],
            }
        ]
    },
    {
        "treatment_id": "234",
        "disease": "DiseaseA",
        "severity": "High",
        "rank": [{"WHO": 4, "NICE": 1}],
        "medication": [
            {
                "name": "Drug67",
                "exclusion": [],
            }
        ]
    },
    {
        "treatment_id": "345",
        "disease": "DiseaseA",
        "severity": "High",
        "rank": [{"WHO": 3, "NICE": 3}],
        "medication": [
            {
                "name": "Drug45",
                "exclusion": [],
            }
        ]
    },
    {
        "treatment_id": "B",
        "disease": "DiseaseA",
        "severity": "High",
        "rank": [{"WHO": 2, "NICE": 2}],
        "medication": [
            {
                "name": "Drug3",
                "exclusion": [],
            }
        ]
    },
    {
        "treatment_id": "C",
        "disease": "DiseaseB",
        "severity": "Low",
        "rank": [{"WHO": 3, "NICE": 5}],
        "medication": [
            {
                "name": "Drug4",
                "exclusion": ["ConditionY"],
            }
        ]
    },
    {
        "treatment_id": "D",
        "disease": "DiseaseB",
        "severity": "Low",
        "rank": [{"WHO": 6, "NICE": 2}],
        "medication": [
            {
                "name": "Drug5",
                "exclusion": ["ConditionX", "ConditionZ"],
            },
            {
                "name": "Drug6",
                "exclusion": ["ConditionX", "ConditionZ"],
            }
        ]
    },
    {
        "treatment_id": "E",
        "disease": "DiseaseB",
        "severity": "High",
        "rank": [{"WHO": 1, "NICE": 2}],
        "medication": [
            {
                "name": "Drug7",
                "exclusion": ["ConditionA"],
            }
        ]
    },
    {
        "treatment_id": "F",
        "disease": "DiseaseA",
        "severity": "Low",
        "rank": [{"WHO": 2, "NICE": 1}],
        "medication": [
            {
                "name": "Drug8",
                "exclusion": ["ConditionB"],
            }
        ]
    },
    {
        "treatment_id": "123",
        "disease": "pneumonia",
        "severity": "high",
        "rank": [{"WHO": 1, "NICE": 2}],
        "medication": [
            {
                "name": "amoxicillin",
                "brand": ["amoxil", "drug1234"], 
                "exclusion": ["pregnant", "penicillin"],
                "form": "solid",
                "unit": "film tablet",
                "splittable": True,
                "admin_route": "oral",
                "dosage": [
                    {
                        "strength_per_unit": 250,
                        "quantity_of_unit": 1,
                        "adult_dose": 500,
                        "pediatric_dose": 0.2,
                        "frequency": "Every 6 hours",
                        "duration": "7 days"
                    }
                ]
            },
            {
                "name": "Co-amoxiclav",
                "brand": ["augmentin", "drug1234"], 
                "exclusion": [],
                "form": "solid",
                "unit": "liquid",
                "splittable": False,
                "admin_route": "intravenous",
                "dosage": [
                    {
                        "strength_per_unit": 4,
                        "quantity_of_unit": 2,
                        "adult_dose": 4,
                        "pediatric_dose": 0.2,
                        "frequency": "Every 6 hours",
                        "duration": "7 days"
                    }
                ]
            },
        ]
    }
]


treatment_db.insert_multiple(treatment_data)

print("All treatments in the database:")
for treatment in treatment_db:
    print(treatment)

treatment_db.close()

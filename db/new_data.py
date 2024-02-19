from tinydb import TinyDB

new_treatment_db = TinyDB('new_db.json')

new_treatment_data = [
        {
            "treatment_id": "A",
            "indication": "DiseaseA",
            "administration": "mouth",
            "form": "tablet",
            "eligibility": [
                {
                    "severity": "High",
                    "exclusion": ["penicillin", "pregnancy"] 
                }
            ],
            "guideline": {
                "BNF": [
                    {
                        "rank":  1,
                        "strategy_1": [
                            {
                                "patient_profile": {"age_range": {"min": 12, "max": 17}, "min_weight":  20},
                                "medication": [
                                    {
                                        "Amoxicillin": [{"frequency_per_day":  2,"dose_mg":  750,"mg/kg":  40, "notes": "750 mg every  12 hours, dose to be taken with food"}],
                                        "Penicillin": [{"frequency_per_day":  2,"dose_mg":  750,"mg/kg":  40, "notes": "750 mg every  12 hours, dose to be taken with food"}]
                                    }
                                ]    
                            }
                        ],
                        "strategy_2": [
                            {
                                "patient_profile": {"age_range": {"min": 18, "max": 100}, "min_weight":  40},
                                "medication": [
                                    {
                                        "Amoxicillin": [{"frequency_per_day":  2,"dose_mg":  750,"mg/kg":  40, "notes": "750 mg every  12 hours, dose to be taken with food"}]
                                    }
                                ]    
                            }
                        ]
                    }
                ],
                "WHO": [
                    {
                        "rank":  2,
                        "strategy_1": [
                            {
                                "patient_profile": {"age_range": {"min": 12, "max": 17}, "min_weight":  40},
                                "medication": [
                                    {
                                        "Amoxicillin": [{"frequency_per_day":  2,"dose_mg":  750,"mg/kg":  40, "notes": "750 mg every  12 hours, dose to be taken with food"}]
                                    }
                                ]    
                            }
                        ],
                        "strategy_2": [
                            {
                                "patient_profile": {"age_range": {"min": 12, "max": 17}, "min_weight":  40},
                                "medication": [
                                    {
                                        "Amoxicillin": [{"frequency_per_day":  2,"dose_mg":  750,"mg/kg":  40, "notes": "750 mg every  12 hours, dose to be taken with food"}]
                                    }
                                ]    
                            }
                        ]
                    }
                ]
            }
        },
        {
            "treatment_id": "B",
            "indication": "DiseaseA",
            "administration": "mouth",
            "eligibility": [
                {
                    "severity": "High",
                    "exclusion": ["penicillin", "pregnancy"]
                }
            ],
            "guideline": {
                "BNF": [
                    {
                        "rank":  2,
                        "strategy_1": [
                            {
                                "patient_profile": {"age_range": {"min": 12, "max": 17}, "min_weight":  40},
                                "medication": [
                                    {
                                        "Amoxicillin": [{"frequency_per_day":  2,"dose_mg":  750,"mg/kg":  40, "notes": "750 mg every  12 hours, dose to be taken with food"}]
                                    }
                                ]    
                            }
                        ],
                        "strategy_2": [
                            {
                                "patient_profile": {"age_range": {"min": 12, "max": 17}, "min_weight":  40},
                                "medication": [
                                    {
                                        "Amoxicillin": [{"frequency_per_day":  2,"dose_mg":  750,"mg/kg":  40, "notes": "750 mg every  12 hours, dose to be taken with food"}]
                                    }
                                ]    
                            }
                        ]
                    }
                ],
                "WHO": [
                    {
                        "rank":  3,
                        "strategy_1": [
                            {
                                "patient_profile": {"age_range": {"min": 12, "max": 17}, "min_weight":  40},
                                "medication": [
                                    {
                                        "Amoxicillin": [{"frequency_per_day":  2,"dose_mg":  750,"mg/kg":  40, "notes": "750 mg every  12 hours, dose to be taken with food"}]
                                    }
                                ]    
                            }
                        ],
                        "strategy_2": [
                            {
                                "patient_profile": {"age_range": {"min": 12, "max": 17}, "min_weight":  40},
                                "medication": [
                                    {
                                        "Amoxicillin": [{"frequency_per_day":  2,"dose_mg":  750,"mg/kg":  40, "notes": "750 mg every  12 hours, dose to be taken with food"}]
                                    }
                                ]    
                            }
                        ]
                    }
                ]
            }
        },
        {
            "treatment_id": "C",
            "indication": "DiseaseA",
            "administration": "injection",
            "eligibility": [
                {
                    "severity": "High",
                    "exclusion": ["lactation"]
                }
            ],
            "guideline": {
                "BNF": [
                    {
                        "rank":  3,
                        "strategy_1": [
                            {
                                "patient_profile": {"age_range": {"min": 12, "max": 17}, "min_weight":  40},
                                "medication": [
                                    {
                                        "Amoxicillin": [{"frequency_per_day":  2,"dose_mg":  750,"mg/kg":  40, "notes": "750 mg every  12 hours, dose to be taken with food"}]
                                    }
                                ]    
                            }
                        ],
                        "strategy_2": [
                            {
                                "patient_profile": {"age_range": {"min": 12, "max": 17}, "min_weight":  40},
                                "medication": [
                                    {
                                        "Amoxicillin": [{"frequency_per_day":  2,"dose_mg":  750,"mg/kg":  40, "notes": "750 mg every  12 hours, dose to be taken with food"}]
                                    }
                                ]    
                            }
                        ]
                    }
                ],
                "WHO": [
                    {
                        "rank":  1,
                        "strategy_1": [
                            {
                                "patient_profile": {"age_range": {"min": 12, "max": 17}, "min_weight":  40},
                                "medication": [
                                    {
                                        "Amoxicillin": [{"frequency_per_day":  2,"dose_mg":  750,"mg/kg":  40, "notes": "750 mg every  12 hours, dose to be taken with food"}]
                                    }
                                ]    
                            }
                        ],
                        "strategy_2": [
                            {
                                "patient_profile": {"age_range": {"min": 12, "max": 17}, "min_weight":  40},
                                "medication": [
                                    {
                                        "Amoxicillin": [{"frequency_per_day":  2,"dose_mg":  750,"mg/kg":  40, "notes": "750 mg every  12 hours, dose to be taken with food"}]
                                    }
                                ]    
                            }
                        ]
                    }
                ]
            }
        },
        {
            "treatment_id": "D",
            "indication": "DiseaseB",
            "administration": "mouth",
            "eligibility": [
                {
                    "severity": "Low",
                    "exclusion": ["penicillin", "pregnancy"]
                }
            ],
            "guideline": {
                "BNF": [
                    {
                        "rank":  1,
                        "strategy_1": [
                            {
                                "patient_profile": {"age_range": {"min": 12, "max": 17}, "min_weight":  40},
                                "medication": [
                                    {
                                        "Amoxicillin": [{"frequency_per_day":  2,"dose_mg":  750,"mg/kg":  40, "notes": "750 mg every  12 hours, dose to be taken with food"}]
                                    }
                                ]    
                            }
                        ],
                        "strategy_2": [
                            {
                                "patient_profile": {"age_range": {"min": 12, "max": 17}, "min_weight":  40},
                                "medication": [
                                    {
                                        "Amoxicillin": [{"frequency_per_day":  2,"dose_mg":  750,"mg/kg":  40, "notes": "750 mg every  12 hours, dose to be taken with food"}]
                                    }
                                ]    
                            }
                        ]
                    }
                ],
                "WHO": [
                    {
                        "rank":  3,
                        "strategy_1": [
                            {
                                "patient_profile": {"age_range": {"min": 12, "max": 17}, "min_weight":  40},
                                "medication": [
                                    {
                                        "Amoxicillin": [{"frequency_per_day":  2,"dose_mg":  750,"mg/kg":  40, "notes": "750 mg every  12 hours, dose to be taken with food"}]
                                    }
                                ]    
                            }
                        ],
                        "strategy_2": [
                            {
                                "patient_profile": {"age_range": {"min": 12, "max": 17}, "min_weight":  40},
                                "medication": [
                                    {
                                        "Amoxicillin": [{"frequency_per_day":  2,"dose_mg":  750,"mg/kg":  40, "notes": "750 mg every  12 hours, dose to be taken with food"}]
                                    }
                                ]    
                            }
                        ]
                    }
                ]
            }
        },
        {
            "treatment_id": "E",
            "indication": "DiseaseB",
            "administration": "injection",
            "eligibility": [
                {
                    "severity": "Low",
                    "exclusion": ["aspirin", "lactation"]
                }
            ],
            "guideline": {
                "BNF": [
                    {
                        "rank":  2,
                        "strategy_1": [
                            {
                                "patient_profile": {"age_range": {"min": 12, "max": 17}, "min_weight":  40},
                                "medication": [
                                    {
                                        "Amoxicillin": [{"frequency_per_day":  2,"dose_mg":  750,"mg/kg":  40, "notes": "750 mg every  12 hours, dose to be taken with food"}]
                                    }
                                ]    
                            }
                        ],
                        "strategy_2": [
                            {
                                "patient_profile": {"age_range": {"min": 12, "max": 17}, "min_weight":  40},
                                "medication": [
                                    {
                                        "Amoxicillin": [{"frequency_per_day":  2,"dose_mg":  750,"mg/kg":  40, "notes": "750 mg every  12 hours, dose to be taken with food"}]
                                    }
                                ]    
                            }
                        ]
                    }
                ],
                "WHO": [
                    {
                        "rank":  2,
                        "strategy_1": [
                            {
                                "patient_profile": {"age_range": {"min": 12, "max": 17}, "min_weight":  40},
                                "medication": [
                                    {
                                        "Amoxicillin": [{"frequency_per_day":  2,"dose_mg":  750,"mg/kg":  40, "notes": "750 mg every  12 hours, dose to be taken with food"}]
                                    }
                                ]    
                            }
                        ],
                        "strategy_2": [
                            {
                                "patient_profile": {"age_range": {"min": 12, "max": 17}, "min_weight":  40},
                                "medication": [
                                    {
                                        "Amoxicillin": [{"frequency_per_day":  2,"dose_mg":  750,"mg/kg":  40, "notes": "750 mg every  12 hours, dose to be taken with food"}]
                                    }
                                ]    
                            }
                        ]
                    }
                ]
            }
        },
        {
            "treatment_id": "F",
            "indication": "DiseaseB",
            "administration": "mouth",
            "eligibility": [
                {
                    "severity": "Low",
                    "exclusion": ["penicillin", "pregnancy"]
                }
            ],
            "guideline": {
                "BNF": [
                    {
                        "rank":  3,
                        "strategy_1": [
                            {
                                "patient_profile": {"age_range": {"min": 12, "max": 17}, "min_weight":  40},
                                "medication": [
                                    {
                                        "Amoxicillin": [{"frequency_per_day":  2,"dose_mg":  750,"mg/kg":  40, "notes": "750 mg every  12 hours, dose to be taken with food"}]
                                    }
                                ]    
                            }
                        ],
                        "strategy_2": [
                            {
                                "patient_profile": {"age_range": {"min": 12, "max": 17}, "min_weight":  40},
                                "medication": [
                                    {
                                        "Amoxicillin": [{"frequency_per_day":  2,"dose_mg":  750,"mg/kg":  40, "notes": "750 mg every  12 hours, dose to be taken with food"}]
                                    }
                                ]    
                            }
                        ]
                    }
                ],
                "WHO": [
                    {
                        "rank":  1,
                        "strategy_1": [
                            {
                                "patient_profile": {"age_range": {"min": 12, "max": 17}, "min_weight":  40},
                                "medication": [
                                    {
                                        "Amoxicillin": [{"frequency_per_day":  2,"dose_mg":  750,"mg/kg":  40, "notes": "750 mg every  12 hours, dose to be taken with food"}]
                                    }
                                ]    
                            }
                        ],
                        "strategy_2": [
                            {
                                "patient_profile": {"age_range": {"min": 12, "max": 17}, "min_weight":  40},
                                "medication": [
                                    {
                                        "Amoxicillin": [{"frequency_per_day":  2,"dose_mg":  750,"mg/kg":  40, "notes": "750 mg every  12 hours, dose to be taken with food"}]
                                    }
                                ]    
                            }
                        ]
                    }
                ]
            }
        }
    ]

new_treatment_db.insert_multiple(new_treatment_data)
new_treatment_db.close()



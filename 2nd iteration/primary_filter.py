from tinydb import TinyDB, Query

def filter_by_disease(diagnosis):
    db = TinyDB('treatment_db.json')
    Treatment = Query()
    treatments = db.search(Treatment.disease.test(lambda x: x.lower() == diagnosis.lower()))
    return treatments

#primary filter for primary diagnosis and comorbidity.

"""def filter_by_disease(diagnosis):
    db = TinyDB('treatment_db.json')
    Treatment = Query()
    treatments = db.search(Treatment.disease == diagnosis)
    return treatments"""
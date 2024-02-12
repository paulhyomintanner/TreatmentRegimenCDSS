from tinydb import TinyDB, Query
def filter_treatments(diagnosis, severity, exclusions=[]):
    db = TinyDB('treatment_db.json')

    Treatment = Query()
    treatments = db.search((Treatment.disease == diagnosis) & (Treatment.severity == severity))

    # once severity and diagnosis have been dealth with , apply the exclusion criteria. 
    treatments = [treatment for treatment in treatments if not any(exclusion in medication.get('exclusion', []) for medication in treatment['medication'] for exclusion in exclusions)]

    return treatments
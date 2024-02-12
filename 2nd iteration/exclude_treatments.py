from tinydb import TinyDB, Query
def filter_by_exclusions(treatments, exclusions):
    return [treatment for treatment in treatments if not any(exclusion in medication.get('exclusion', []) for medication in treatment['medication'] for exclusion in exclusions)]

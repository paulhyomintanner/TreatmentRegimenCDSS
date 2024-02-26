from tinydb import TinyDB

superseding_rules_db = TinyDB('superseding_rules_db.json')

rules = [
    {"pair": ["A", "D"], "superseding_id": "A"},
    {"pair": ["A", "F"], "superseding_id": "F"},
    {"pair": ["A", "E"], "superseding_id": "E"}
]

superseding_rules_db.insert_multiple(rules)
superseding_rules_db.close()






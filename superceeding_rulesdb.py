from tinydb import TinyDB

def initialize_rules_db(rules_db_path='flexible_rules_db.json'):
    db = TinyDB(rules_db_path)

    rules = [
        {"pair": ["A", "D"], "superseding_id": "A"},
        {"pair": ["B", "C"], "superseding_id": "B"}
    ]

    db.insert_multiple(rules)

    print(f"Initialized and populated the rules database at '{rules_db_path}' with flexible rules.")

initialize_rules_db()



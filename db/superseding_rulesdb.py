from tinydb import TinyDB

def initialize_rules_db(rules_db_path='superseding_rules_db.json'):
    db = TinyDB(rules_db_path)

    rules = [
        {"pair": ["A", "D"], "superseding_id": "A"},
        {"pair": ["B", "C"], "superseding_id": "B"},
        {"pair": ["A", "E"], "superseding_id": "E"}
    ]

    db.insert_multiple(rules)

    print(f"Initialized rules database at '{rules_db_path}'.")

initialize_rules_db()






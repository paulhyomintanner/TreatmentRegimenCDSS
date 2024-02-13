class Treatment:
    def __init__(self, name, indications, rank, drugs=None, exclusions=None, eligible_for_all=True):
        self.name = name
        self.indications = indications
        self.drugs = drugs if drugs else []
        self.exclusions = exclusions if exclusions else []
        self.eligible_for_all = eligible_for_all
        self.rank = rank

    def add_drug(self, drug_name):
        self.drugs.append(drug_name)

    def add_indication(self, disease, severity):
        self.indications.append((disease, severity))

    def is_eligible(self, disease, severity):
        for indication in self.indications:
            if indication == (disease, severity):
                return True
        return False

    def __repr__(self):
        indications_str = ', '.join([f"({disease}, {severity})" for disease, severity in self.indications])
        return f"Treatment(name='{self.name}', drugs={self.drugs}, indications=[{indications_str}], exclusions={self.exclusions}, eligible_for_all={self.eligible_for_all}, rank={self.rank})"
import customtkinter as ctk
import tkinter.messagebox as messagebox
import tkinter as tk
import json
import math


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

class Data:
    def __init__(self):
        self.data = self.load_data()
        self.rules = self.load_superseding_rules()
        
    def load_data(self):
        with open('RealCPG.json') as f:
            data = json.load(f)
        return data
    
    def load_superseding_rules(self):
        with open('superseding_rules_db.json') as f:
            rules = json.load(f)
        return rules

    def map_disease_to_severity(self):
        disease_to_severity = {}
        for treatment in self.data['_default'].values():
            disease = treatment['disease']
            severities = set()
            for eligibility in treatment['eligibility']:
                for severity_type, severity_value in eligibility['severity'].items():
                    severities.add(f"{severity_type}: {severity_value}")
            if disease in disease_to_severity:
                disease_to_severity[disease].update(severities)
            else:
                disease_to_severity[disease] = severities
        return {disease: sorted(severities) for disease, severities in disease_to_severity.items()}
    
class SimpleRulesEngine:
    def __init__(self, rules_file=None):
        self.rules = self.load_rules(rules_file) if rules_file else []

    def load_rules(self, rules_file):
        with open(rules_file, 'r') as file:
            return json.load(file)

    def evaluate(self, recommended_treatments, user_data):
        warnings = []
        for rule in self.rules:
            if self._matches(rule["conditions"], recommended_treatments, user_data):
                warnings.append(rule["action"])
        return warnings

    def _matches(self, conditions, recommended_treatments, user_data):
        for disease, treatment in recommended_treatments.items():
            if 'medication' in treatment:  
                for medication in treatment['medication']:  
                    if conditions.get('medication') == medication.get('drug'):  
                        if "user_medication" in conditions:
                            if conditions["user_medication"] in user_data.get("medications", []):  
                                return True
        return False

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        data_instance = Data()
        self.data = data_instance.data
        self.rules = data_instance.rules
        self.disease_to_severity = data_instance.map_disease_to_severity()
        self.rejected_treatments = []
        self.strategy_checkboxes = {}
        self.confirmed_strategies = []
        self.rules_engine = SimpleRulesEngine()
        self.superseded_info = {}

        
        self.user_data = {
        "weight": None,
        "height": None,
        "age": None, 
        "cpg": None,
        "diseases": []
    }
        #UI page setup and widgets
        self.geometry("1000x700")
        self.title("Treatment Regimen CDSS")
        self.minsize(300, 200)

        self.grid_rowconfigure(list(range(30)), weight=1)
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)

        self.input_frame = ctk.CTkFrame(master=self)
        self.input_frame.grid(row=0, rowspan=30, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        self.input_frame.grid_rowconfigure(list(range(20)), weight=1)
        self.input_frame.grid_columnconfigure((0,1), weight=1)

        self.exclusion_frame = ctk.CTkScrollableFrame(self.input_frame)
        self.exclusion_frame.grid(row=13, column=0, rowspan=7, columnspan=2, padx=10, pady=10, sticky="nsew")
        self.exclusion_frame.grid_rowconfigure((0, 1), weight=1)
        self.exclusion_frame.grid_columnconfigure((0,1), weight=1)

        self.treatment_frame = ctk.CTkFrame(master=self)
        self.treatment_frame.grid(row=0, rowspan=30, column=2, columnspan=2, padx=10, pady=10, sticky="nsew")
        self.treatment_frame.grid_rowconfigure(list(range(30)), weight=1)
        self.treatment_frame.grid_columnconfigure((0,1), weight=1)

        self.frame = ctk.CTkScrollableFrame(self.treatment_frame)
        self.frame.grid(row=20, rowspan=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.user_input_label = ctk.CTkLabel(self.input_frame, text="Step 1: Input Data", font=("Arial", 14, "bold"))
        self.user_input_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

        self.cpg_label = ctk.CTkLabel(self.input_frame, text="Select CPG:", font=("Arial", 12, "bold"))
        self.cpg_label.grid(row=1, column=0, padx=10, pady=1)
        cpgs = list(set(cpg for treatment in self.data['_default'].values() for cpg in treatment['rank'][0]))
        self.cpg_dropdown = ctk.CTkOptionMenu(self.input_frame, values=cpgs)
        self.cpg_dropdown.grid(row=2, column=0, padx=10, pady=3, sticky="nsew")

        self.height_label = ctk.CTkLabel(self.input_frame, text="Enter Patient Height:", font=("Arial", 12, "bold"))
        self.height_label.grid(row=3, column=0, padx=10, pady=1, sticky="ew")
        self.height_entry = ctk.CTkEntry(self.input_frame, placeholder_text="Height")
        self.height_entry.grid(row=4, column=0, padx=10, pady=3, sticky="ew")

        self.weight_label = ctk.CTkLabel(self.input_frame, text="Enter Patient Weight:", font=("Arial", 12, "bold"))
        self.weight_label.grid(row=5, column=0, padx=10, pady=1, sticky="ew")
        self.weight_entry = ctk.CTkEntry(self.input_frame, placeholder_text="Weight")
        self.weight_entry.grid(row=6, column=0, padx=10, pady=3, sticky="ew")

        self.age_label = ctk.CTkLabel(self.input_frame, text="Enter Patient Age:", font=("Arial", 12, "bold"))
        self.age_label.grid(row=7, column=0, padx=10, pady=1, sticky="ew")
        self.age_entry = ctk.CTkEntry(self.input_frame, placeholder_text="Age")
        self.age_entry.grid(row=8, column=0, padx=10, pady=3, sticky="ew")
        
        exclusions = list(set(exclusion for treatment in self.data['_default'].values() for eligibility in treatment['eligibility'] for exclusion in eligibility['exclusion']))
        self.exclusions = ctk.CTkLabel(self.input_frame, text="Select exclusions that apply:")
        self.exclusions.grid(row=11, column=0, padx=3, pady=5)

        self.exclusion_checkboxes = {}
        for i, exclusion in enumerate(exclusions):
            cb = ctk.CTkCheckBox(self.exclusion_frame, text=exclusion)
            cb.grid(row=0 + i, column=0, sticky="nsew")
            self.exclusion_checkboxes[exclusion] = cb

        diseases = list(self.disease_to_severity.keys())
        self.diseases_label = ctk.CTkLabel(self.input_frame, text="Select disease:")
        self.diseases_label.grid(row=21, column=0, padx=10, pady=5)
        self.disease_var = tk.StringVar()
        self.disease_dropdown = ctk.CTkOptionMenu(self.input_frame, variable=self.disease_var, values=diseases, command=self.update_severity_dropdown)
        self.disease_dropdown.grid(row=21, column=1, padx=10, pady=5, sticky="ew")

        self.severity_label = ctk.CTkLabel(self.input_frame, text="Select severity:")
        self.severity_label.grid(row=22, column=0, padx=10, pady=5)
        self.severity_var = tk.StringVar()
        self.severity_dropdown = ctk.CTkOptionMenu(self.input_frame, variable=self.severity_var, values=[])
        self.severity_dropdown.grid(row=22, column=1, padx=10, pady=5, sticky="ew")

        self.medication_label = ctk.CTkLabel(self.input_frame, text="Add existing patient medication:", font=("Arial", 12, "bold"))
        self.medication_label.grid(row=1, column=1, padx=10, pady=1, sticky="ew")
        self.medication_entry = ctk.CTkEntry(self.input_frame, placeholder_text="Current medication (separated by commas)")
        self.medication_entry.grid(row=2, column=1, padx=10, pady=3, sticky="ew")

        self.pre_existing_conditions_entry = ctk.CTkEntry(self.input_frame, placeholder_text="Pre-existing conditions")
        self.pre_existing_conditions_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

        self.treatments_label = ctk.CTkLabel(self.treatment_frame, text="Step 2: Confirm or Reject Treatment Regimens", font=("Arial", 14, "bold"))
        self.treatments_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

        self.display_textbox = ctk.CTkTextbox(self.treatment_frame, height=280, width=300)
        self.display_textbox.grid(row=1, column=0, columnspan=2, rowspan=14, padx=10, pady=10, sticky="nsew")
        self.display_textbox.configure(state=tk.DISABLED)

        self.submit_button = ctk.CTkButton(self.input_frame, text="Click to submit disease (selection displayed below)", command=self.submit_disease)
        self.submit_button.grid(row=24, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        self.display_treatment_selection = ctk.CTkTextbox(self.input_frame, height=50, width=300)
        self.display_treatment_selection.grid(row=25, column=0, columnspan=2, rowspan=3, padx=10, pady=10, sticky="nsew")
        self.display_treatment_selection.configure(state=tk.DISABLED)

        
        self.button = ctk.CTkButton(self.input_frame, text="Retrieve Treatments", command=self.button_callback)
        self.button.grid(row=30, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        self.confirm_treatment_button = ctk.CTkButton(self.treatment_frame, text="Confirm Treatment", command=self.retrieve_strategies)
        self.confirm_treatment_button.grid(row=17, column=0, columnspan=2, padx=5, pady=10, sticky="ew")

        self.step_3_label = ctk.CTkLabel(self.treatment_frame, text="Step 3: Select Treatment Strategies", font=("Arial", 14, "bold"))
        self.step_3_label.grid(row=18, column=0, columnspan=2, padx=1, pady=1, sticky="ew")
        self.step_3_explanation = ctk.CTkLabel(self.treatment_frame, text="Select strategies for each medication you require and enter drug concentration if applicable")
        self.step_3_explanation.grid(row=19, column=0, columnspan=2, padx=1, pady=1, sticky="ew")

        self.rejection_label = ctk.CTkLabel(self.treatment_frame, text="Enter treatment ID(s) then press enter to reject")
        self.rejection_label.grid(row=15, column=0, columnspan=2, padx=1, pady=1, sticky="ew")
        self.reject_treatment_entry = ctk.CTkEntry(self.treatment_frame, placeholder_text="Enter treatment ID(s) to reject")
        self.reject_treatment_entry.grid(row=16, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
        self.reject_treatment_entry.bind("<Return>", self.handle_rejection)

        self.strategy_label = ctk.CTkLabel(self.treatment_frame, text="Recommended Strategies (select and enter drug concentration)")
        self.strategy_label.grid(row=27, column=0, columnspan=2, padx=1, pady=1, sticky="ew")

        self.confirm_strategies_button = ctk.CTkButton(self.treatment_frame, text="Confirm Strategies and Generate Regimen", command=self.confirm_strategies)
        self.confirm_strategies_button.grid(row=28, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        self.reset_button = ctk.CTkButton(self.treatment_frame, text="Reset", command=self.reset)
        self.reset_button.grid(row=30, column=0, columnspan=1, padx=10, pady=10, sticky="ew")


    def reset(self):
        self.user_data = {
            'weight': 0,
            'height': 0,
            'age': 0,
            'cpg': '',
            'diseases': [],
            'medications': [],
            'pre_existing_conditions': [],
            'exclusions': []
        }

        self.display_treatment_selection.configure(state=tk.NORMAL)
        self.display_treatment_selection.delete('1.0', tk.END)
        self.display_treatment_selection.configure(state=tk.DISABLED)

        self.display_textbox.configure(state=tk.NORMAL)
        self.display_textbox.delete('1.0', tk.END)
        self.display_textbox.configure(state=tk.DISABLED)

        self.height_entry.delete(0, tk.END)
        self.weight_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.medication_entry.delete(0, tk.END)

        for checkbox in self.strategy_checkboxes.values():
            checkbox.destroy()
        self.strategy_checkboxes.clear()

        for entry in self.concentration_entries.values():
            entry.destroy()
        self.concentration_entries.clear()     
   
    def handle_rejection(self,event):
        rejected_ids = self.reject_treatment_entry.get().split(',')  
        self.user_data['exclusions'].extend(rejected_ids)  
        self.rejected_treatments.extend(rejected_ids) 
        self.reject_treatment_entry.delete(0, tk.END)
        self.retrieve_treatments() 


    def retrieve_strategies(self):
        row_offset = len(self.exclusion_checkboxes)
        processed_strategies = set()  

        for disease, treatment in self.recommended_treatments.items():
            treatment_id = treatment.get('treatment_id')
            for medication in treatment.get('medication', []):
                medication_name = medication.get('drug')
                for dose_strategy in medication.get('dose_strategy', []):
                    strategy = dose_strategy.get('strategy')
                    therapeutic_dose = dose_strategy.get('therapeuticDose', 'N/A')

                    strategy_identifier = f"{treatment_id}_{medication_name}_{strategy}_{therapeutic_dose}" 

                    if strategy_identifier not in processed_strategies: 
                        processed_strategies.add(strategy_identifier)  

                        strategy_var = tk.BooleanVar()
                        strategy_text = f"{medication_name}, {treatment_id}, Strategy: {strategy}, Therapeutic dose: {therapeutic_dose}, \nEnter Concentration (mg/unit):"
                        strategy_cb = ctk.CTkCheckBox(self.frame, text=strategy_text, variable=strategy_var)
                        strategy_cb.grid(row=10 + row_offset, column=2, padx=10, pady=2, sticky="nsew")
                        self.strategy_checkboxes[(treatment_id, medication_name, strategy)] = strategy_cb  

                        if medication['form']['divisible']: 
                            concentration_entry = ctk.CTkEntry(self.frame)
                            concentration_entry.grid(row=10 + row_offset, column=3, padx=10, pady=2, sticky="nsew")
                        
                            if hasattr(self, 'concentration_entries'):
                                self.concentration_entries[(treatment_id, medication_name, strategy)] = concentration_entry
                            else:
                                self.concentration_entries = {(treatment_id, medication_name, strategy): concentration_entry}                 
                        row_offset += 1

    def calculate_bsa(self, height, weight):    
        return math.sqrt((height * weight) / 3600)

    def calculate_dose_based_on_weight(self, weight, doseQuantity):
        return weight * doseQuantity

    def calculate_dose_based_on_bsa(self, bsa, doseQuantity):
        return bsa * doseQuantity

    def check_max_dose(self, dose, max_dose):
        if dose > max_dose:
            return max_dose
        return dose

    def calculate_dose_per_administration(self, dose, frequency):
        return dose / frequency


    def confirm_strategies(self):
        confirmed_strategies = []
        for (treatment_id, medication_name, strategy), checkbox_var in self.strategy_checkboxes.items():
            if checkbox_var.get():  
                concentration = 0  
                if (treatment_id, medication_name, strategy) in self.concentration_entries:  
                    concentration_entry = self.concentration_entries[(treatment_id, medication_name, strategy)]
                    concentration_str = concentration_entry.get()
                    if concentration_str:  
                        try:
                            concentration = float(concentration_str)
                        except ValueError:
                            print(f"Invalid concentration entered for strategy {strategy} in treatment {treatment_id}")
                            continue
                confirmed_strategies.append({
                    'treatment_id': treatment_id,
                    'medication': medication_name,
                    'strategy': strategy,
                    'concentration': concentration
                })
        print(confirmed_strategies)
        print(self.recommended_treatments)
        self.confirmed_strategies = confirmed_strategies
        self.calculate_personalized_treatment_plan()


    def calculate_personalized_treatment_plan(self):
        treatment_to_diseases = {}
        for disease, treatment_details in self.recommended_treatments.items():
            if 'treatment_id' in treatment_details:
                treatment_id = treatment_details['treatment_id']
            else:
                treatment_id = None  
            if treatment_id not in treatment_to_diseases:
                treatment_to_diseases[treatment_id] = [disease]
            else:
                treatment_to_diseases[treatment_id].append(disease)

        popup_window = ctk.CTkToplevel(self)
        popup_window.title("Personalized Treatment Plan")
        popup_window.geometry("600x400")

        treatment_text_widget = ctk.CTkTextbox(popup_window, width=580, height=380, state='normal')
        treatment_text_widget.pack(padx=10, pady=10)

        for treatment_id, diseases in treatment_to_diseases.items():
            treatment_details = next((t for d, t in self.recommended_treatments.items() if 'treatment_id' in t and t['treatment_id'] == treatment_id), None)
            if treatment_details:
                diseases_text = ", ".join(diseases)  
                treatment_text_widget.insert('end', f"Diseases: {diseases_text}\nTreatment ID: {treatment_details['treatment_id']}\nDescription: {treatment_details['description']}\n")
                

                for medication in treatment_details.get('medication', []):
                    for dose_strategy in medication.get('dose_strategy', []):
                        confirmed_strategy = next((item for item in self.confirmed_strategies if item['treatment_id'] == treatment_details['treatment_id'] and item['medication'] == medication['drug'] and item['strategy'] == dose_strategy['strategy']), None)
                        if confirmed_strategy:
                            strategy = dose_strategy.get('strategy')
                            frequency = dose_strategy.get('timing', {}).get('repeat', {}).get('frequency', 1)
                            concentration = confirmed_strategy.get('concentration', 0)
                            dose_info_text = f"Strategy: {strategy}\n"

                            if strategy in ["weight", "bsa", "single dose"]:
                                if strategy == "weight":
                                    dose = self.calculate_dose_based_on_weight(self.user_data['weight'], dose_strategy['doseAndRate'][0]['doseQuantity']['value'])
                                elif strategy == "bsa":
                                    bsa = self.calculate_bsa(self.user_data['height'], self.user_data['weight'])
                                    dose = self.calculate_dose_based_on_bsa(bsa, dose_strategy['doseAndRate'][0]['doseQuantity']['value'])
                                elif strategy == "single dose":
                                    dose = dose_strategy['doseAndRate'][0]['doseQuantity']['value']



                                max_dose = dose_strategy.get('maxDosePerPeriod', {}).get('numerator', {}).get('value', float('inf'))
                                dose = min(dose, max_dose)
                                #dose_per_administration = self.calculate_dose_per_administration(dose, frequency) if isinstance(dose, (int, float)) else "N/A"
                                
                                if concentration > 0:
                                    volume_per_dose = dose / concentration
                                    dose_info_text += f"Volume per Dose: {volume_per_dose:.2f} units (ml/tablet)\n"
                                
                                dose_info_text += f"Calculated Dose: {dose}mg\nDose per Administration: {dose} mg\n"

                            treatment_text_widget.insert(
                                'end',
                                f"Medication: {medication['drug']}\nForm: {medication['form']['type']}\nSite: {medication['site']}\nRoute: {medication['route']}\nMethod: {medication['method']}\n{dose_info_text}Instruction: {dose_strategy['instruction']}\nPatient Instruction: {dose_strategy['patientInstruction']}\nMax Dose: {dose_strategy['maxDosePerPeriod']['numerator']['value']} {dose_strategy['maxDosePerPeriod']['numerator']['unit']} per {dose_strategy['maxDosePerPeriod']['denominator']['value']} {dose_strategy['maxDosePerPeriod']['denominator']['unit']}\n\n")

        treatment_text_widget.configure(state='disabled')
        
        close_button = ctk.CTkButton(popup_window, text="Close", command=popup_window.destroy)
        close_button.pack(pady=10)


    def update_severity_dropdown(self, selected_disease):
        severities = self.disease_to_severity.get(selected_disease, [])
        self.severity_dropdown.destroy()
        self.severity_dropdown = ctk.CTkOptionMenu(self.input_frame, variable=self.severity_var, values=severities)
        self.severity_dropdown.grid(row=22, column=1, padx=10, pady=5)
        if severities:
            self.severity_var.set(severities[0])
        else:
            self.severity_var.set('')

    def get_exclusions(self):
        selected_exclusions = []
        for exclusion, checkbox in self.exclusion_checkboxes.items():
            if checkbox.get() == 1: 
                selected_exclusions.append(exclusion)
        return selected_exclusions

    def get_medications(self):
        medications = [medication.strip() for medication in self.medication_entry.get().split(',') if medication.strip()]
        self.user_data['medications'] = medications

    def get_pre_existing_conditions(self):
        pre_existing_conditions = [condition.strip() for condition in self.pre_existing_conditions_entry.get().split(',') if condition.strip()]
        self.user_data['pre_existing_conditions'] = pre_existing_conditions

    def submit_disease(self):
        disease = self.disease_dropdown.get()
        severity = self.severity_var.get()  
        self.user_data["diseases"].append({"disease": disease, "severity": severity})

        self.display_treatment_selection.configure(state=tk.NORMAL)
        self.display_treatment_selection.insert('end', f"Disease: {disease}, Severity: {severity}\n")
        self.display_treatment_selection.configure(state=tk.DISABLED)

        print(self.user_data)  

    def get_weight(self):
        try:
            weight = float(self.weight_entry.get())
            self.user_data['weight'] = weight
        except ValueError:
            print("Invalid weight entered")

    def get_height(self):
        try:
            height = float(self.height_entry.get())
            self.user_data['height'] = height
        except ValueError:
            print("Invalid height entered")

    def get_age(self):  
        try:
            age = int(self.age_entry.get())
            self.user_data['age'] = age
        except ValueError:
            print("Invalid age entered")

    def button_callback(self):
        self.get_medications()
        self.get_pre_existing_conditions()
        self.get_weight()
        self.get_height()
        self.get_age()
        self.user_data.update({
            "exclusions": self.get_exclusions(),
            "cpg": self.cpg_dropdown.get(),
        })
        print(self.user_data)  

        self.retrieve_treatments()

    def filter_by_disease(self, treatments, disease):
        return [treatment for treatment in treatments if treatment['disease'] == disease]

    def rank_treatments(self, treatments, preferred_cpg):
        return sorted(treatments, key=lambda x: x['rank'][0][preferred_cpg])
    
    def filter_treatments_by_severity(self, treatments, user_severity):
        filtered_treatments = []
        for treatment in treatments:
            for eligibility in treatment.get('eligibility', []):
                if self.matches_severity(eligibility.get('severity', {}), user_severity):
                    filtered_treatments.append(treatment)
        return filtered_treatments
    
    def matches_severity(self, eligibility_severity, user_severity):
        for key, values in eligibility_severity.items():
            if isinstance(values, list):
                for value in values:
                    if user_severity == f"{key}: {value}":
                        return True
            else:
                if user_severity == f"{key}: {values}":
                    return True
        return False

    def filter_by_exclusions(self, treatments, exclusions):
        return [treatment for treatment in treatments 
            if not any(any(exclusion in eligibility.get('exclusion', []) 
                        for exclusion in exclusions) for eligibility in treatment['eligibility'])]


    def filter_patient_profile(self, treatments, age_entry, weight_entry):
        return [treatment for treatment in treatments for eligibility in treatment['eligibility']
            if eligibility['patient_profile']['age_range']['min'] <= age_entry <= eligibility['patient_profile']['age_range']['max'] 
            and weight_entry >= eligibility['patient_profile']['min_weight']]
    
    
    def apply_superseding_rules(self, candidate_treatments):
        superseding_rules = self.rules["_default"]
        recommended_treatments = {}
        superseded_info = {}  

        treatment_to_diseases = {}
        for disease, treatment in candidate_treatments.items():
            treatment_id = treatment.get('treatment_id')
            if treatment_id not in treatment_to_diseases:
                treatment_to_diseases[treatment_id] = [disease]
            else:
                treatment_to_diseases[treatment_id].append(disease)

        for rule in superseding_rules.values():
            pair = rule["pair"]
            superseding_id = rule["superseding_id"]
            
            if all(treatment_id in treatment_to_diseases for treatment_id in pair):
                for treatment_id in pair:
                    for disease in treatment_to_diseases.get(treatment_id, []):
                        recommended_treatments[disease] = next((t for t in candidate_treatments.values() if t.get('treatment_id') == superseding_id), candidate_treatments[disease])
                        if treatment_id != superseding_id:  
                            superseded_info[disease] = {"superseded": treatment_id, "superseding": superseding_id}
            else:
                for treatment_id in pair:
                    diseases = treatment_to_diseases.get(treatment_id, [])
                    for disease in diseases:
                        if disease not in recommended_treatments:  
                            recommended_treatments[disease] = candidate_treatments[disease]

        for disease in candidate_treatments:
            if disease not in recommended_treatments:
                recommended_treatments[disease] = candidate_treatments[disease]

        return recommended_treatments, superseded_info  


    def retrieve_treatments(self):
        self.rules_engine = SimpleRulesEngine(rules_file='interaction_rules.json')
        user_diseases = self.user_data["diseases"]
        candidate_treatments = {}


        for disease_info in user_diseases:
            user_disease = disease_info["disease"]
            user_severity = disease_info["severity"]
            treatments = self.data['_default'].values()
            disease_treatments = self.filter_by_disease(treatments, user_disease)
            severity_filtered_treatments = self.filter_treatments_by_severity(disease_treatments, user_severity)
            patient_eligibility_treatments = self.filter_patient_profile(severity_filtered_treatments, int(self.user_data["age"]), int(self.user_data["weight"]))
            exclusion_filtered_treatments = self.filter_by_exclusions(patient_eligibility_treatments, self.user_data["exclusions"])
            exclusion_filtered_treatments = [treatment for treatment in exclusion_filtered_treatments if treatment['treatment_id'] not in self.rejected_treatments]
            preferred_cpg = self.user_data["cpg"]
            ranked_treatments = self.rank_treatments(exclusion_filtered_treatments, preferred_cpg)
            if ranked_treatments:  
                top_treatment = ranked_treatments[0]  
                candidate_treatments[user_disease] = top_treatment
            else:
                candidate_treatments[user_disease] = {"For Disease": user_disease, "Message": "No treatments found according to specified parameters"}
            
        self.recommended_treatments, superseded_info = self.apply_superseding_rules(candidate_treatments)

        warnings = self.rules_engine.evaluate(self.recommended_treatments, self.user_data)

        self.display_textbox.configure(state=tk.NORMAL)
        self.display_textbox.delete('1.0', tk.END)



        for disease, treatment in self.recommended_treatments.items():
            if 'disease' in treatment and 'treatment_id' in treatment and 'medication' in treatment:
                for med in treatment['medication']:
                    treatment_text = f"Disease: {disease}\nTreatment ID: {treatment['treatment_id']}\nDescription: {treatment['description']}\nMedication: {med['drug']}\nRoute: {med['route']}\nMethod: {med['method']}\nSite: {med['site']}\nForm: {med['form']['type']}\n\n"
                    self.display_textbox.insert(tk.END, treatment_text)  
            else:
                treatment_text = f"{treatment['For Disease']}: {treatment['Message']}\n"
                self.display_textbox.insert(tk.END, treatment_text)


            
            if disease in superseded_info:
                supersession_msg = f"Note: Treatment ID {superseded_info[disease]['superseded']} has been superseded by Treatment ID {superseded_info[disease]['superseding']} for {disease}.\n"
                self.display_textbox.insert(tk.END, supersession_msg)

        self.display_textbox.configure(state=tk.DISABLED)



        if warnings:
            warnings_str = "Warnings:\n"
            for warning in warnings:
                warnings_str += str(warning) + "\n"
            messagebox.showwarning("Warnings", warnings_str)


        self.confirm_treatment_button.grid()
        self.reject_treatment_entry.grid()



if __name__ == "__main__":
    app = App()
    app.mainloop()




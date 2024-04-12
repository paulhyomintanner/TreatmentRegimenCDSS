import flet as ft
from flet import Page, RouteChangeEvent, View, AppBar, Text, ElevatedButton, Dropdown, TextField, Column
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment
import json
import os



def load_data():
    data = {}
    directory = 'CPGs'
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            with open(os.path.join(directory, filename)) as f:
                key = filename[:-5]  
                data[key] = json.load(f)
    return data



def load_superseding_rules():
    with open('superseding_rules_db.json') as f:
        rules = json.load(f)
    return rules

def main(page: Page) -> None:
    page.title = 'CDSS Regimen Builder'
    page.window_width = 350
    page.window_height = 700

    user_data = {
        'weight': 0,
        'height': 0,
        'dob': [],
        'cpg': '',
        'diseases': [],
        'medications': [],
        'exclusions': []
    }
    


    cpgdata = load_data()
    print(cpgdata)
    rules = load_superseding_rules()
    selected_cpg = []
    selected_cpg_data = {}  
    candidate_treatments = {}


    def route_change(e: RouteChangeEvent) -> None:
        nonlocal selected_cpg, selected_cpg_data  
        page.views.clear()
        selected_cpg = []

        
        def confirm_cpg(e):
            nonlocal selected_cpg, selected_cpg_data  
            selected_cpg = e.control.value
            selected_cpg_data = cpgdata[selected_cpg]
            user_data['cpg'] = selected_cpg  
            print(selected_cpg_data)


        cpg_options = [ft.dropdown.Option(key) for key in cpgdata.keys()]
        cpgdropdown = Dropdown(label='CPG', options=cpg_options, on_change=confirm_cpg)
        confirm_cpg_button = ElevatedButton(text='Confirm', on_click=lambda _: page.go('/UserInput'))

        page.views.append(
            View(
                route='/',
                controls=[
                    Text(value='Select CPG', size=30),
                    cpgdropdown,
                    confirm_cpg_button
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=20
            )
        )

        
        dob_input = TextField(label="Insert Date of Birth (DD/MM/YYYY)", width=200)
        weight_input = TextField(label="Insert Patient Weight (kg)", width=200)
        height_input = TextField(label="Insert Patient Height (cm)", width=200)


        def get_user_data(e):
            user_data['dob'] = dob_input.value
            user_data['weight'] = weight_input.value
            user_data['height'] = height_input.value
            page.go('/Exclusions')
            print(user_data)


        if page.route == '/UserInput':
            page.views.append(
            View(
                route='/UserInput',
                controls=[
                    Text(value='User input', size=30),
                    ElevatedButton(text='Go back', on_click=lambda _: page.go('/')),
                    dob_input,
                    weight_input,
                    height_input,
                    ElevatedButton(text='Next', on_click=get_user_data)
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=20
            )
        )
            
        def update_severity_options(e):
            """
            Updates the severity options dropdown based on the selected disease, this is found in the selected_cpg_data.

            Parameters:
                e (Event): The event object that triggered the function, in this case the selection of the disease from
                the disease drop down menu.

            Returns:
                None
            """
            selected_disease = e.control.value
            unique_severities = set()


            for treatment in selected_cpg_data['_default'].values():
                if treatment['disease'] == selected_disease:
                    for eligibility in treatment['eligibility']:
                        for key, value in eligibility['severity'].items():
                            severity = f"{key}: {value}"  
                            unique_severities.add(severity)

            severity_options = [ft.dropdown.Option(severity) for severity in sorted(unique_severities)]
            
            severity_dd.options = severity_options
            severity_dd.update()  




        if '_default' in selected_cpg_data:
            unique_exclusions = {exclusion for treatment in selected_cpg_data['_default'].values() for eligibility in treatment['eligibility'] for exclusion in eligibility['exclusion']}
            unique_diseases = {treatment['disease'] for treatment in selected_cpg_data['_default'].values()}            
            disease_options = [ft.dropdown.Option(disease) for disease in sorted(unique_diseases)]
            disease_dd = Dropdown(label='Disease Criteria', options=disease_options, on_change=update_severity_options)

            severity_dd = Dropdown(label="Add severity", options=[])

            exclusion_options = [ft.dropdown.Option(exclusion) for exclusion in sorted(unique_exclusions)]
            exclusion_dd = Dropdown(label='Exclusion Criteria', options=exclusion_options)
        
        def get_disease_data(e):
            """Once the submit button is clicked then the function will get the selected disease and severity and add it to the 
            user_data dictionary. This way the user can add as many diseases as they want.
            
            Parameters:
                e (Event): The event object that triggered the function is the submit button click, in this case the selection of the disease from
                the disease drop down menu.

            Returns:
                None
            """
            disease_severity = {
                'disease': disease_dd.value,
                'severity': severity_dd.value
            }
            user_data['diseases'].append(disease_severity)
            disease_severity_text.value += f"Selected: {disease_severity.values()}\n"
            print(user_data)
            page.update()

        def add_exclusions(e):
            user_data['exclusions'].append(exclusion_dd.value)
            exclusion_text.value += f"Selected: {exclusion_dd.value}\n"
            print(user_data)
            page.update()


        submit_disease_button = ElevatedButton(text='Add Disease', on_click=get_disease_data, height=25)
        add_exclusion_button = ElevatedButton(text='Add Exclusion', on_click=add_exclusions, height=25)
        disease_severity_text = Text(value='')
        exclusion_text = Text(value='')


        scroll_container =ft.Container(
            content= ft.Column(
                            controls=[
                                disease_severity_text,
                                exclusion_text
                            ],
                            height=130,
                            width=350,
                            spacing=5, 
                            scroll=ft.ScrollMode.ALWAYS
                            ),
            width=350,
            height=200,
            bgcolor=ft.colors.INDIGO_100,
            border=ft.border.all(1, ft.colors.BLACK),
            border_radius=ft.border_radius.all(5),
            padding=ft.padding.all(10)
        )

        def get_treatments(e):
            page.go('/SelectTreatmentPlan')
            

        if page.route == '/Exclusions':
            page.views.append(
                View(
                    route='/Exclusions',
                    controls=[
                        Text(value='Input Exclusions', size=30),
                        Column(
                            controls=[
                                disease_dd,
                                severity_dd,
                                submit_disease_button,          
                                exclusion_dd,
                                add_exclusion_button, 
                                scroll_container,                 
                            ],
                        spacing=10,
                        height=500,
                        width=350,
                        scroll=ft.ScrollMode.ALWAYS
                        ),
                        ElevatedButton(text='Next', height=30, on_click=get_treatments),
                        ElevatedButton(text='Go back', height=30,on_click=lambda _: page.go('/UserInput')) 
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=10
                )
            )


        from datetime import datetime

        def calculate_age_in_days_and_years(birth_date_str):
            try:
                birth_date = datetime.strptime(birth_date_str, '%d/%m/%Y')
            except ValueError as e:
                print(f"Error parsing DOB: {e}. Ensure the format is DD/MM/YYYY.")
                return None, None  

            today_date = datetime.today()
            age_in_days = (today_date - birth_date).days
            age_in_years = today_date.year - birth_date.year - ((today_date.month, today_date.day) < (birth_date.month, birth_date.day))

            print(f"Parsed DOB: {birth_date}")  #Debugging 
            print(f"Today's Date: {today_date}")  
            print(f"Age in Days: {age_in_days}, Age in Years: {age_in_years}")  

            return age_in_days, age_in_years
        


        def check_superseding_rules(highest_ranked_treatments, rules):
            treatments_dict = {t['treatment_id']: t for t in highest_ranked_treatments}
            for rule_details in rules['_default'].values():
                pair = rule_details['pair']
                superseding_id = rule_details['superseding_id']

                #Check if both treatments in the pair are present in the highest ranked treatments list
                if all(treatment_id in treatments_dict for treatment_id in pair):
                    #If a pair is found, determine which one is superseded
                    for treatment_id in pair:
                        if treatment_id != superseding_id:
                            diseaseA = treatments_dict[treatment_id]['disease']
                            diseaseB = treatments_dict[superseding_id]['disease']
                            superseding_rule = f"Superseding Rule Triggered: {rule_details}"
                            message = f"Treatment {superseding_id} can be used for both {diseaseA} and {diseaseB}."
                            return (treatments_dict[superseding_id], superseding_rule, message)
            return (None, "No superseding rules apply.", None)


        """
        def check_superseding_rules(highest_ranked_treatments, rules):
            treatments_dict = {t['treatment_id']: t for t in highest_ranked_treatments}
            for rule_details in rules['_default'].values():
                pair = rule_details['pair']
                superseding_id = rule_details['superseding_id']

                # Check if both treatments in the pair are present in the highest ranked treatments list
                if all(treatment_id in treatments_dict for treatment_id in pair):
                    # If a pair is found, determine which one is superseded
                    for treatment_id in pair:
                        if treatment_id != superseding_id:
                            diseaseA = treatments_dict[treatment_id]['disease']
                            diseaseB = treatments_dict[superseding_id]['disease']
                            superseding_rule = f"Superseding Rule Triggered: {rule_details}"
                            message = f"Treatment {superseding_id} can be used for both {diseaseA} and {diseaseB}"
                            return (superseding_id, superseding_rule, message)
            return ([t['treatment_id'] for t in highest_ranked_treatments], "No superseding rules applied.", None)
        """
        """
        def retrieve_treatments(user_data, selected_cpg_data):
            user_diseases = user_data['diseases']
            user_dob = user_data['dob']  
            age_in_days, age_in_years = calculate_age_in_days_and_years(user_dob)  
            user_weight = int(user_data['weight'])
            user_exclusions = user_data['exclusions']

            highest_ranked_treatments = []

            for user_disease in user_diseases:
                disease_name = user_disease['disease']
                disease_severity = user_disease['severity']
                eligible_treatments = []

                for treatment in selected_cpg_data['_default'].values():
                    if treatment['disease'] == disease_name:
                        for eligibility in treatment['eligibility']:
                            severity_condition = f"{list(eligibility['severity'].keys())[0]}: {list(eligibility['severity'].values())[0]}"
                            if disease_severity == severity_condition:
                                patient_profile = eligibility['patient_profile']
                                age_range_unit = patient_profile.get('age_range_unit', 'years')
                                age_range = patient_profile['age_range']
                                min_weight = patient_profile.get('min_weight', 0)
                                exclusions = eligibility['exclusion']

                                user_age = age_in_days if age_range_unit == 'days' else age_in_years

                                if (age_range['min'] <= user_age <= age_range['max'] and 
                                    user_weight >= min_weight and 
                                    not any(exclusion in user_exclusions for exclusion in exclusions)):
                                    eligible_treatments.append(treatment)
                
                if eligible_treatments:                  
                    eligible_treatments.sort(key=lambda x: list(x['rank'][0].values())[0])
                    print(eligible_treatments)
                    highest_ranked_treatments.append(eligible_treatments[0])
                    print(highest_ranked_treatments)

            
            result = check_superseding_rules(highest_ranked_treatments, rules)
            if result[2]: 
                recommended_treatments_text.value = (result[1])  # Print the rule triggered
                print(recommended_treatments_text.value)  
            else:
                for treatment_id in result[0]:
                    recommended_treatments_text.value = f"Recommended treatment: {treatment_id}, ({result[1]})"
                print(recommended_treatments_text.value)  
            page.update()
            return result"""

        """
        def retrieve_treatments(user_data, selected_cpg_data):
            user_diseases = user_data['diseases']
            user_dob = user_data['dob']  
            age_in_days, age_in_years = calculate_age_in_days_and_years(user_dob)  
            user_weight = int(user_data['weight'])
            user_exclusions = user_data['exclusions']

            highest_ranked_treatments = []

            for user_disease in user_diseases:
                disease_name = user_disease['disease']
                disease_severity = user_disease['severity']
                eligible_treatments = []

                for treatment in selected_cpg_data['_default'].values():
                    if treatment['disease'] == disease_name:
                        for eligibility in treatment['eligibility']:
                            severity_condition = "{}: {}".format(list(eligibility['severity'].keys())[0], 
                                                                list(eligibility['severity'].values())[0])
                            if disease_severity == severity_condition:
                                patient_profile = eligibility['patient_profile']
                                age_range_unit = patient_profile.get('age_range_unit', 'years')
                                age_range = patient_profile['age_range']
                                min_weight = patient_profile.get('min_weight', 0)
                                exclusions = eligibility['exclusion']
                                        
                                user_age = age_in_days if age_range_unit == 'days' else age_in_years

                                if (age_range['min'] <= user_age <= age_range['max'] and 
                                    user_weight >= min_weight and 
                                    not any(exclusion in user_exclusions for exclusion in exclusions)):
                                    eligible_treatments.append(treatment)
                        
                if eligible_treatments:
                    eligible_treatments.sort(key=lambda x: list(x['rank'][0].values())[0])
                    highest_ranked_treatments.append(eligible_treatments[0])

            result = check_superseding_rules(highest_ranked_treatments, rules)
            output_text = []

            if result[2]:  # if there is a message about superseding
                output_text.append(result[1])  
                output_text.append(result[2])  
            else:
                # Handle no superseding rule: display all highest ranked treatments
                for treatment in highest_ranked_treatments:
                    treatment_details = f"Recommended treatment: {treatment['treatment_id']} for {treatment['disease']}\nDescription: {treatment['description']}"
                    for medication in treatment['medication']:
                        treatment_details += f"\n  Medication: {medication['drug']}, Form: {medication['form']['type']}, Dose: {medication['dose_strategy'][0]['instruction']}"
                    output_text.append(treatment_details)
                output_text.append(result[1])  

            
            recommended_treatments_text.value = "\n\n".join(output_text)
            print(recommended_treatments_text.value)  
            page.update()
            return result
            """
        
        def retrieve_treatments(user_data, selected_cpg_data):
            user_diseases = user_data['diseases']
            user_dob = user_data['dob']  
            age_in_days, age_in_years = calculate_age_in_days_and_years(user_dob)  
            user_weight = int(user_data['weight'])
            user_exclusions = user_data['exclusions']

            highest_ranked_treatments = []

            for user_disease in user_diseases:
                disease_name = user_disease['disease']
                disease_severity = user_disease['severity']
                eligible_treatments = []

                for treatment in selected_cpg_data['_default'].values():
                    if treatment['disease'] == disease_name:
                        for eligibility in treatment['eligibility']:
                            severity_condition = "{}: {}".format(list(eligibility['severity'].keys())[0], 
                                                                list(eligibility['severity'].values())[0])
                            if disease_severity == severity_condition:
                                patient_profile = eligibility['patient_profile']
                                age_range_unit = patient_profile.get('age_range_unit', 'years')
                                age_range = patient_profile['age_range']
                                min_weight = patient_profile.get('min_weight', 0)
                                exclusions = eligibility['exclusion']
                                        
                                user_age = age_in_days if age_range_unit == 'days' else age_in_years

                                if (age_range['min'] <= user_age <= age_range['max'] and 
                                    user_weight >= min_weight and 
                                    not any(exclusion in user_exclusions for exclusion in exclusions)):
                                    eligible_treatments.append(treatment)
                        
                if eligible_treatments:
                    eligible_treatments.sort(key=lambda x: list(x['rank'][0].values())[0])
                    highest_ranked_treatments.append(eligible_treatments[0])

            result = check_superseding_rules(highest_ranked_treatments, rules)
            output_text = []

            if result[0]:  
                treatment_details = f"{result[1]}\n{result[2]}\nDetailed Information for {result[0]['treatment_id']}:\nDescription: {result[0]['description']}"
                for medication in result[0]['medication']:
                    treatment_details += f"\n  Medication: {medication['drug']}, Form: {medication['form']['type']}, Dose: {medication['dose_strategy'][0]['instruction']}"
                output_text.append(treatment_details)
            else:
                for treatment in highest_ranked_treatments:
                    treatment_details = f"Recommended treatment: {treatment['treatment_id']} for {treatment['disease']}\nDescription: {treatment['description']}"
                    for medication in treatment['medication']:
                        treatment_details += f"\n  Medication: {medication['drug']}, Form: {medication['form']['type']}, Dose: {medication['dose_strategy'][0]['instruction']}"
                    output_text.append(treatment_details)
                output_text.append(result[1])

            recommended_treatments_text.value = "\n\n".join(output_text)
            print(recommended_treatments_text.value)
            page.update()
            return result


        recommended_treatments_text = Text(value='')
 

    
        if page.route == '/SelectTreatmentPlan':
            page.views.append(
            View(
                route='/SelectTreatmentPlan',
                controls=[
                    Column(
                        controls=[
                            Text(value='Select Treatment', size=30),
                            ElevatedButton(text='retrieve treatments', on_click=lambda _: retrieve_treatments(user_data, selected_cpg_data)),
                            ElevatedButton(text='reject treatment'),
                            ElevatedButton(text='Go back', on_click=lambda _: page.go('/Exclusions')),               
                            ElevatedButton(text='Proceed With Treatments', on_click=lambda _: page.go('/SelectDosingStrategy')),
                            recommended_treatments_text,
                        ],
                        height=500,
                        width=350,
                        scroll=ft.ScrollMode.ALWAYS
                    ),
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=20
            )
        )
            
        if page.route == '/SelectDosingStrategy':
            page.views.append(
            View(
                route='/SelectDosingStrategy',
                controls=[
                    Text(value='User input', size=30),
                    ElevatedButton(text='Go back', on_click=lambda _: page.go('/SelectTreatmentPlan')),
                    ElevatedButton(text='Build Regimen', on_click=lambda _: page.go('/BuildRegimen'))
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=20
            )
        )
            
        if page.route == '/BuildRegimen':
            page.views.append(
            View(
                route='/BuildRegimen',
                controls=[
                    Text(value='Personalized regimen', size=30),
                    ElevatedButton(text='Restart', on_click=lambda _: page.go('/'))
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=20
            )
        )
            
        page.update()

    def view_pop(e: ViewPopEvent) -> None:
        page.views.pop()
        top_view: View = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
        
    

if __name__ == "__main__":
    ft.app(target=main)





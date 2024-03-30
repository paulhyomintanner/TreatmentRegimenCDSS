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

    user_data = {
        'weight': 0,
        'height': 0,
        'age': 0,
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

    def route_change(e: RouteChangeEvent) -> None:
        nonlocal selected_cpg, selected_cpg_data  
        page.views.clear()
        selected_cpg = []

        
        def confirm_cpg(e):
            nonlocal selected_cpg, selected_cpg_data  
            selected_cpg = e.control.value
            selected_cpg_data = cpgdata[selected_cpg]
            user_data['cpg'] = selected_cpg  
            print(selected_cpg, selected_cpg_data)


        cpg_options = [ft.dropdown.Option(key) for key in cpgdata.keys()]
        cpgdropdown = Dropdown(label='CPG', options=cpg_options, on_change=confirm_cpg)
        confirm_cpg_button = ElevatedButton(text='Confirm', on_click=lambda _: page.go('/UserInput'))

        page.views.append(
            View(
                route='/',
                controls=[
                    AppBar(title=Text('Start'), bgcolor='blue'),
                    Text(value='Select CPG', size=30),
                    cpgdropdown,
                    confirm_cpg_button
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=20
            )
        )


        age_input = TextField(label="Insert Patient Age")
        weight_input = TextField(label="Insert Patient Weight (kg)")
        height_input = TextField(label="Insert Patient Height (cm)")




        def get_user_data(e):
            user_data['age'] = age_input.value
            user_data['weight'] = weight_input.value
            user_data['height'] = height_input.value
            page.go('/Exclusions')
            print(user_data)


        if page.route == '/UserInput':
            page.views.append(
            View(
                route='/UserInput',
                controls=[
                    AppBar(title=Text('User input'), bgcolor='blue'),
                    Text(value='User input', size=30),
                    ElevatedButton(text='Go back', on_click=lambda _: page.go('/')),
                    age_input,
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
            disease_severity = {
                'disease': disease_dd.value,
                'severity': severity_dd.value
            }
            user_data['diseases'].append(disease_severity)
            disease_severity_text.value += f"Selected: {disease_severity.values()}\n"
            print(user_data)
            page.update()

        submit_disease_button = ElevatedButton(text='Add Disease', on_click=get_disease_data)
        disease_severity_text = Text(value='')

        if page.route == '/Exclusions':
            page.views.append(
            View(
                route='/Exclusions',
                controls=[
                    AppBar(title=Text('Input Exclusions'), bgcolor='blue'),
                    Text(value='Input Exclusions', size=30),
                    disease_dd,
                    severity_dd,
                    submit_disease_button,   
                    disease_severity_text,        
                    exclusion_dd,                    
                    ElevatedButton(text='Next', on_click=lambda _: page.go('/SelectTreatmentPlan')),
                    ElevatedButton(text='Go back', on_click=lambda _: page.go('/UserInput'))
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=20
            )
        )
            
        if page.route == '/SelectTreatmentPlan':
            page.views.append(
            View(
                route='/SelectTreatmentPlan',
                controls=[
                    AppBar(title=Text('Select Treatment Plan'), bgcolor='blue'),
                    Text(value='Select Treatment', size=30),
                    ElevatedButton(text='reject treatment'),
                    ElevatedButton(text='Go back', on_click=lambda _: page.go('/Exclusions')),               
                    ElevatedButton(text='Proceed Without Rejections', on_click=lambda _: page.go('/SelectDosingStrategy'))
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
                    AppBar(title=Text('Select Dosing Strategy'), bgcolor='blue'),
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
                    AppBar(title=Text('Personalized Regimen'), bgcolor='blue'),
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

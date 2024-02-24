import flet as ft

def main(page: ft.Page):
    page.title = "Disease Selection"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    diseases = ["Disease A", "Disease B", "Disease C"]

    disease_dropdown = ft.Dropdown(
        label="Select a disease",
        options=[ft.dropdown.Option(text=disease) for disease in diseases]  
    )

    def disease_selected(e):
        selected_disease = disease_dropdown.value
        print(f"Selected Disease: {selected_disease}")

    
    disease_dropdown.on_change = disease_selected

    page.add(disease_dropdown)

ft.app(target=main)

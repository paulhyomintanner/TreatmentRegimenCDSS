from typing import Optional, List

class SimpleQuantity:
  """Represents a quantity with a value and unit."""
  def __init__(self, value: float, unit: str):
      self._value = value
      self._unit = unit

  @property
  def value(self) -> float:
      return self._value

  @property
  def unit(self) -> str:
      return self._unit

class Dose(SimpleQuantity):
  """Represents a dosage with base dose, unit, and whether it's per kilogram."""
  def __init__(self, base_dose: float, unit: str, per_kg: bool = False):
      super().__init__(base_dose, unit)
      self._per_kg = per_kg

  def calculate_dose(self, weight: Optional[float] = None) -> float:
      """Calculates the dose based on the weight."""
      if self._per_kg and weight is not None:
          return self._value * weight
      return self._value

  @property
  def per_kg(self) -> bool:
      return self._per_kg

class RouteOfAdministration:
  """Represents a route of administration with a route."""
  def __init__(self, route: str):
      self._route = route

  @property
  def route(self) -> str:
      return self._route

class MedicationForm:
  """Represents a medication form with a form."""
  def __init__(self, form: str):
      self._form = form

  @property
  def form(self) -> str:
      return self._form

class Ingredient:
  """Represents an ingredient in a medication."""
  def __init__(self, name: str):
      self._name = name

  @property
  def name(self) -> str:
      return self._name

class Allergy:
  """Represents an allergy with an ingredient."""
  def __init__(self, ingredient: Ingredient):
      self._ingredient = ingredient

  @property
  def ingredient(self) -> Ingredient:
      return self._ingredient

class Regimen:
  """Represents a Regimen with a form, route of administration, dosage, frequency, duration, and rate."""
  def __init__(self, form: MedicationForm, route_of_administration: RouteOfAdministration, dosage: Dose, frequency: str, duration: int, rate: str):
      self._form = form
      self._route_of_administration = route_of_administration
      self._dosage = dosage
      self._frequency = frequency
      self._duration = duration
      self._rate = rate

  def get_Regimen_info(self, weight: Optional[float] = None) -> str:
      calculated_dose = self._dosage.calculate_dose(weight)
      regimen_info = f"{self._form.form}, Route: {self._route_of_administration.route}, Dosage: {calculated_dose} {self._dosage.unit}, Frequency: {self._frequency}, Duration: {self._duration} days"
      if self._rate and self._form.form.lower() == "liquid" and self._route_of_administration.route.lower() == "iv":
         regimen_info += f", Rate: {self._rate}"
      return regimen_info

class Treatment:
  """Base class for Medication and Brand."""
  def __init__(self, name: str):
      self._name = name
      self._children = []

  def add_child(self, child: 'Treatment'):
      """Adds a child to the Treatment."""
      self._children.append(child)

  @property
  def name(self) -> str:
      return self._name

  @property
  def children(self) -> List['Treatment']:
      return self._children

class Brand(Treatment):
  """Represents a brand with a brand name and Regimens."""
  def add_Regimen(self, Regimen: Regimen):
      """Adds a Regimen to the brand."""
      self.add_child(Regimen)

class Medication(Treatment):
  """Represents a medication with a generic name, brands, and ingredients."""
  def __init__(self, name: str):
      super().__init__(name)
      self._ingredients = []

  def add_brand(self, brand: Brand):
      """Adds a brand to the medication."""
      self.add_child(brand)

  def add_ingredient(self, ingredient: Ingredient):
      """Adds an ingredient to the medication."""
      self._ingredients.append(ingredient)

  @property
  def ingredients(self) -> List[Ingredient]:
      return self._ingredients

class Disease:
  """Represents a disease with a name, ICD-11 code, and severity scale."""
  def __init__(self, name: str, icd_11_code: str, severity_scale: str):
      self._name = name
      self._icd_11_code = icd_11_code
      self._severity_scale = severity_scale

  @property
  def name(self) -> str:
      return self._name

  @property
  def severity_scale(self) -> str:
      return self._severity_scale



class DiseaseMedicationLink:
    def __init__(self, medication: Medication, Regimen: Regimen, priority: int):
        self._medication = medication
        self._Regimen = Regimen
        self._priority = priority

    @property
    def medication(self) -> Medication:
        return self._medication


    @property
    def priority(self) -> int:
        return self._priority

    def get_medication_info(self, weight: float) -> str:
        medication_name = self._medication.name
        Regimen_info = self._Regimen.get_Regimen_info(weight)
        return f"{medication_name} - {Regimen_info}"

class Patient:
  def __init__(self, diagnosis: Disease, weight: float):
      self._diagnosis = diagnosis
      self._weight = weight
      self._allergies = []

  def add_allergy(self, allergy: Allergy):
      """Adds an allergy to the patient."""
      self._allergies.append(allergy)

  @property
  def allergies(self) -> List[Allergy]:
      return self._allergies

  @property
  def diagnosis(self) -> Disease:
      return self._diagnosis

  @property
  def weight(self) -> float:
      return self._weight

class TreatmentPlan:
  def __init__(self):
      self._disease_to_medication_map = {}

  def add_medication_link(self, disease_name: str, severity_scale: str, link: DiseaseMedicationLink):
      key = f"{disease_name}-{severity_scale}"
      if key not in self._disease_to_medication_map:
          self._disease_to_medication_map[key] = []
      self._disease_to_medication_map[key].append(link)

  def build_treatment_plan_for_patient(self, patient: Patient) -> List[str]:
      """Builds a treatment plan for a patient."""
      key = f"{patient.diagnosis.name}-{patient.diagnosis.severity_scale}"
      medication_links = sorted(self._disease_to_medication_map.get(key, []), key=lambda x: x.priority)
      plan = []
      for link in medication_links:
          if not any(allergy.ingredient.name in ingredient.name for allergy in patient.allergies for ingredient in link.medication.ingredients):
                plan.append(link.get_medication_info(patient.weight))
                break
      if not plan:
          print("No medication found due to allergy.")
      else:
          return plan

if __name__ == "__main__":
    weight = float(input("Enter patient's weight (kg):\n"))
    patient_disease = input("Enter patient's disease:\n")
    disease_severity = input("Enter disease severity (moderate/high):\n")
    allergy_input = input("Enter any known drug allergies (e.g., Penicillin, None):\n")

    # Initialize Treatment Plan
    treatment_plan = TreatmentPlan()

    # Medications
    co_amoxiclav = Medication("Co-Amoxiclav")
    amoxicillin = Medication("Amoxicillin")
    doxycycline = Medication("Doxycycline")

    # Ingredients
    penicillin = Ingredient("Penicillin")
    co_amoxiclav.add_ingredient(penicillin)
    amoxicillin.add_ingredient(penicillin)

    # Brands and Regimens
    # Co-Amoxiclav for high severity pneumonia
    co_amoxiclav_brand = Brand("Augmentin")
    co_amoxiclav_regimen = Regimen(MedicationForm("Liquid"), RouteOfAdministration("IV"), Dose(1000, "mg", per_kg=False), "Twice daily", 10, "20 ml/hour")
    co_amoxiclav_brand.add_Regimen(co_amoxiclav_regimen)

    # Amoxicillin for moderate severity pneumonia
    amoxicillin_brand = Brand("Amoxil")
    amoxicillin_regimen = Regimen(MedicationForm("Capsule"), RouteOfAdministration("Oral"), Dose(5, "mg", per_kg=True), "Three times daily", 10, "N/A")
    amoxicillin_brand.add_Regimen(amoxicillin_regimen)

    # Doxycycline for patients with Penicillin allergy
    doxycycline_brand = Brand("Vibramycin")
    doxycycline_regimen = Regimen(MedicationForm("Tablet"), RouteOfAdministration("Oral"), Dose(100, "mg", per_kg=False), "Once daily", 10, "N/A")
    doxycycline_brand.add_Regimen(doxycycline_regimen)

    # Disease-Medication Links
    pneumonia_co_amoxiclav_high_link = DiseaseMedicationLink(co_amoxiclav, co_amoxiclav_regimen, 1)
    pneumonia_doxycycline_high_link = DiseaseMedicationLink(doxycycline, doxycycline_regimen, 2)
    pneumonia_amoxicillin_moderate_link = DiseaseMedicationLink(amoxicillin, amoxicillin_regimen, 1)
    pneumonia_doxycycline_moderate_link = DiseaseMedicationLink(doxycycline, doxycycline_regimen, 2)

    # Adding Links to Treatment Plan
    treatment_plan.add_medication_link("Pneumonia", "high", pneumonia_co_amoxiclav_high_link)
    treatment_plan.add_medication_link("Pneumonia", "moderate", pneumonia_amoxicillin_moderate_link)
    treatment_plan.add_medication_link("Pneumonia", "moderate", pneumonia_doxycycline_moderate_link)
    treatment_plan.add_medication_link("Pneumonia", "high", pneumonia_doxycycline_high_link)

    # Sample Patient with Allergy
    patient_allergies = []
    if allergy_input.lower() == "penicillin":
        patient_allergies.append(Allergy(penicillin))

    patient = Patient(Disease(patient_disease, "Unknown-ICD-Code", disease_severity), weight)
    for allergy in patient_allergies:
        patient.add_allergy(allergy)

    # Building Treatment Plan
    plan = treatment_plan.build_treatment_plan_for_patient(patient)
    print(f"Treatment Plan for {patient_disease} ({disease_severity}):")
    for item in plan:
        print(item)

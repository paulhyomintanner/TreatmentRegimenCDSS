# TreatmentRegimenCDSS
Thesis topic on dynamically selecting treatment regimens for clinicians. Disclaimer Warning: The data and treatments are not to be used as actual treatments and are fake. They are for testing the Proof of concept only and for demonstrative purposes. All patient data is fake and all treatment suggestions, dosing strategies, and patient data is fake and dummy and should not be used to influence treatment decisions. 

To test the Tkinter application (iteration5), clone the repository. Then run the `iteration5.py` script to use the GUI. 
Dependencies: customtkinter, tkinter, json, math, os, and sys
![Screenshot 2025-03-02 132857](https://github.com/user-attachments/assets/14ac1a1e-33e0-4d6e-9fee-0fec91bc3499)


[MSMI_Tanner_Paul_Poster.pdf](https://github.com/user-attachments/files/19043181/MSMI_Tanner_Paul_Poster.pdf)


## Test case for superseding treatments: 

### Step 1: Input Data 
1. input - Select `GhanaSTG`
2. input - Enter patient details: height: 120, weight: int > 10, age: 8, current medication: empty, Exclusions: Select none. 
3. input - Select `Pneumonia` and `CURB-65 >2` then click submit.
4. input - Select `Acute Otitis Media` and `Seriousness Low` then click submit.
5. click - click `retrieve Treatments`

### Step 2: Confirm or Reject Treatment Regimens
1. Acute Otitis Media will have treatment `AC`. Scroll down for Pneumonia:
   "Treatment id: Note: Treatment ID A has been superseded by Treatment ID AC for Acute Otitis Media"
2. If you want to reject a treatment, type it into the "Enter Treatment ID(s) to reject" input, and press enter.
   The process will re-run again minus the rejected treatments, and provide different treatment options until the list is exhausted.
   If `AC` is rejected, then `Pneumonia` will have a new treatment recommendation `AD`, and Acute Otitis Media will have `A`.
3. Click `Confirm treatment` when you are happy with the recommendations.

### Step 3: Select Treatment Strategies 
1. Select the medication you want to be part of the treatment plan and if you want, the concentration of the medication - mg/unit. 
   - if the dosing strategy is "single dose" then the medication will not be dosed even if the dose is given in mg/kg
   - if the dosing strategy is "weight" then the patient dose will be calculated per weight.
2. Click "Confirm Strategies and Generate Regimen" - The regimen will pop up in a separate window.

- To trigger a warning: add "weferin" to "add existing patient medication:" and if a treatment contains penicillin then it will be triggered.
- Exclusion criteria will narrow down treatment selection. They are arbitrary for now - needs to be updated. 

## Test case for ratios:

### Step 1: Input Data 
1. input - Select `MSF_CPG`
2. input - Enter patient details: height: 40, weight: 20, age: 5, current medication: empty, Exclusions: Select none. 
3. input - Select `Acute Otitis Media` Seriousness: High then click submit.
5. click - click `retrieve Treatments`

### Step 2: Confirm or Reject Treatment Regimens
1. Acute Otitis Media will have treatment will be treatment: `MSF 2`
2. Confirm treatment

### Step 3:  Select Treatment Strategies 
1. Add treatment strategies and add concentration, then confirm strategy.
   - the ratio will be calculated according to the therapeutic dose for the main drug. In this case, Amoxicillin. 


Link to video on the ratios: [https://youtu.be/ussRG5I1eiU](https://youtu.be/ussRG5I1eiU)

- CPGs are found in the `CPGs` folder

## Test case for superseding treatments with Flet: 

To test the Flet application (iteration 6), clone the repository. Then run the `iteration6.py` script. 
Dependencies: json, math, os, sys, flet (version 0.19.0 only - pip install flet==0.19.0)
Link to video demonstration of the test case: https://youtu.be/oC-VRhtK05M


### Step 1: Input Patient data
1. input - Select `MSF_3` - (other CPGs have not been updated to the final data model)
2. input - Enter patient details: height: 50, weight: 2, dob: 'date the that makes patient 4 days old', current medication: empty, Exclusions: Select none.
3. Click 'next' 
4. input - Select `Bacterial Meningitis` and `Seriousness: Moderate Severity` then click add disease.
5. input - Select `Acute Otitis Media` and `Seriousness: Low Severity` then click add disease.
6. click - click `next`. Below is an example of a dummy patient for testing - it should not be used to treat a patient.
   ![input](https://github.com/user-attachments/assets/f7e660c2-f4cb-473f-8c59-503aed88e3ec)
   


### Step 2: Confirm or Reject Treatment Regimens
1. Click 'retrieve treatments' - given the above inputs a a rule will be printed and a treatment superseded
2. If you want to reject the treatment then select the radio button and click submit. Confirmation will be printed below
   The process will re-run again minus the rejected treatments, and provide different treatment options until the list is exhausted.
   A new treatment will be recommended 
3. Click `Proceed with displayed treatments` when you are happy with the recommendations.

### Step 3: Select Treatment Strategies 
1. Click "Get dosing strategies".
2. Select the medication you want to be part of the treatment plan and if displayed the concentration of the medication - mg/unit. 
3. Click "Submit Choices" then click 'Proceed to Regimen'. Below is an example of a dummy treatment strategy. Disclaimer: This is fake information and should not be used to treat a patient. 
![dose](https://github.com/user-attachments/assets/9a15a7cc-065e-416d-b36c-d0c2e35b6c60)

### Step 4: Generate Regimen
1. Click on "Build Regimen", and the display will be print the personalised treatment regimen. Disclaimer: Below is a fake treatment suggestion and it should not be used to treat a patient. 
![regimen](https://github.com/user-attachments/assets/28a466ae-cdb6-437d-8199-9441b4d4acf2)


### sources for testing data
1. Acute otitis media (AOM) | MSF Medical Guidelines. (2024). https://medicalguidelines.msf.org/en/viewport/CG/english/acute-otitis-media-aom-16689234.html
2. Bacterial meningitis | MSF Medical Guidelines. (2024). https://medicalguidelines.msf.org/en/viewport/CG/english/bacterial-meningitis-16689907.html
3. Acute pneumonia | MSF Medical Guidelines. (2024). https://medicalguidelines.msf.org/en/viewport/CG/english/acute-pneumonia-16689522.html
4. Africa Centres for Disease Control and Prevention. (2021b, November 19). African Antibiotic Treatment Guidelines for common bacterial infections and syndromes - Recommended antibiotic treatments in neonatal and pediatric patients – Africa CDC. Africa CDC. https://africacdc.org/download/african-antibiotic-treatment-guidelines-for-common-bacterial-infections-and-syndromes-recommended-antibiotic-treatments-in-neonatal-and-pediatric-patients/
5. Republic of Ghana Ministry of Health Standard Treatment Guidelines (2017)https://www.moh.gov.gh/wp-content/uploads/2016/02/Standard-Treatment-Guideline-2010.pdf


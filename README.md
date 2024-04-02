# TreatmentRegimenCDSS
Thesis topic on dynamically selecting treatment regimens for clinicians.

To test clone the repositiory. Then run the poc.py script to use the gui. 

Test case for superseding treatments: 

Step 1: Input Data 
    1. input - Select GhanaSTG
    2. input - Enter patient details: height: 120, weight: int > 10, age: 8, current medication: empty, Exclusions: Select none. 
    3. input - Select Pneumonia and CURB-65 >2 then click submit.
    4. input - Select Acute Otitis Media Seriousness: High then click submit.
    5. click - click retrieve Treatments

Step 2: Confirm or Reject Treatment Regimens
    1. Acute Otitis Media will have have treatment AC. Scroll down for Pneumonia:
    "Treatment id: Note: Treatment ID A has been superseded by Treatment ID AC for Acute Otitis Media"
    2. If you want to reject a treatment, type it into the "Enter Treatmen ID(s) to reject" input, and press enter.
    The process will re-run again minus the rejected treatments, and provide different treatment options until the list is exhausted.
    IF AC is rejected, then Pneumonia will have a new treatment recommendation "AD", and Acute Otitis Media will have "A".
    3. Click Confirm treatment when you are happy with the recommendations.

Step 3: Select Treatment Strategies 
    1. Select the medication you want to be part of the treatment plan and if you want, the concentration of the medication - mg/unit. 
    - if the dosing strategy is "single dose" then the medication will not be dosed even if the dose is given in mg/kg
    - if the dosing strategy is "weight" then the the patient dose will be calculated per weight.
    2. Click "Confirm Strategies and Generate Regimen" - The regimen will pop up in a seperate window.


- To trigger warning: add "weferin" to "add existing patient medication:" and if a treatment contains penicillin then it will be triggered.
- Exclusion criteria will narrow down treatment selection. They are arbitrary for now - needs to be updated. 

Test case for ratios:

Step 1: Input Data 
    1. input - Select MSF_CPG
    2. input - Enter patient details: height: 40, weight: 20, age: 5, current medication: empty, Exclusions: Select none. 
    3. input - Select Acute Otitis Media Seriousness: High then click submit.
    5. click - click retrieve Treatments

Step 2: Confirm or Reject Treatment Regimens
    1. Acute Otitis Media will have have treatment will be treatment: MSF 2
    2. Confirm treatment

Step 3:  Select Treatment Strategies 
    1. Add treatment strategies and add concentration, then confirm strategy.
    - the ratio will be calculated acording to the therapeutic dose for the main drug. In this case Amoxicillin. 
    - Currently the "calculated dose" is just for the primary drug, but that will be changed. 

Changes that will  be made:
- clear up dosing strategies
- add more information for user to decide on treatment
- Currently the "calculated dose" is just for the primary drug, but that will be changed. 

link to video on the ratios: https://youtu.be/ussRG5I1eiU


- CPGs are found in the CPGs folder
- Flet folder contains ui changes that would be implmented if time permits - not finished. 



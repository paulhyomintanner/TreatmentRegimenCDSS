Points (16.02.23) After first process.
Feedback:
Filtering : 
The first disease - severity filter. The eligibility attribute is not being used at all at this time in case you are confused. 
You can add the comorbidity as well if needed/wanted.
PDXX: As discussed I think having a pre-filter just on diagnostic will improve performance, Eligibility comes after (Severity, ...  )  the comorbidity is an interesting point, in a sense in can be part of the diagnostic list (pre-filter) and eligibility; this makes me wonder if the "Diagnostic" should not be a list where several diagnostic/comorbidity could be specified for a given treatment

Exclusion filter:
I think what might make sense is if the user is prompted to select some exclusions from a list potentially? So that the input can be verified. 
Because for now you can type anything in and if it matches the exclusion for the treatment then it is excluded. 
PDXX: for me this is exactly as eligibility: a strategy that is defined in details on the execution layer, so the current approach is good to me.
       
Ranking:
I am unsure how to rank the treatments. But I presume that a clinician will have to rank treatments based on priority at some point based on
their expertise/ or clinical guidelines. I  just made a rudimentary ranking attribute for now that is used to sort the list. 
I put the ranking after the exclusion and again after the user exclusion which re-ranks them.
PDXX: I think we are on the same page, ranking comes from superseding and "rank", could also be called priority or intention order,; basically for a given guideline (MSF, WHO, ICRC ... ) treatment for a same "diagnosic" should have different priority. regarding the implementation the priority could be a number (as done today on github) or a series of relationships like superseding. After the User exclusion it should loop back to the previous stages: rank and check superseding based on the new treatment candidates.

For now the treatment candidate list is then printed in the console itself for the sake of simplicity. 
The next process would be  the rules for succeeding etc and the postcoordination. Then the validation and regimen builder, which I started on a while ago.
PDXX: that is perfectly fine for a POC

few points:
-  I think the exclusion and eligibility can be check in the same step, they are the two side of the same coin; they are only required because it is easier to human to think that way
-  I thought "User Treatment Exclusion" should be after the ranking (and loop back to ranking in case of refusal) to avoid asking too much questions and mislead user by giving a drug name that they might not get but I will double check my colleagues


Changes made from 1st iteration:
- added CPG guidline (NICE and WHO) that changes the rank of the treatments based on regional CPG (country specific)
- added db for treatments
- added ranking after the user exclusion
- superseding rules database added to handle the rules - if comorbidity is present.
- basic dosage calculation added. 
- created the primary filter for selecting and ranking diseases seperate from exclusion. 

Questions:
- How to deal with postcoordination. 
- Treatment based database - contains the treatment for one specific disease and its related attributes. 
    - Want to make treatments available for other diseases? - dosing information, form, admin, etc. may change as a result. 
- Dosing strategies: Can do different dosing guidelines as an example (similar to guidelines for treatment recommendation?) NICE guidelines for neonate etc.
    - make a database for the formula used to calculate dose?
    - add a drug unit calculation?
     or just print the corresponding guideline?

Actions:

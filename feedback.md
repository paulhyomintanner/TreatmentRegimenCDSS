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

- have the superceding before the the user exclusion. only display top ranked treatment. The user exclusion wil only be the top ranked treatments being displayed.
- This will move the user acceptance of the treatment plan from before the drug is calculated to before that to after the superceding rules. 
- Once the user has accepted the treatment 
- Change the data structure from "exclusion" and "severity" as seperate lists, into a dictionary called "eligibility". Add post-coordination as a aligibility. 
- change the dosing strategies from "neonate" etc, into the "dosing strategies" e.g. anti-biotic peak strategy, > 50's strategy. 
- simple dosing strategy. 

- key changes - data structure, dosing strategies, post-coordination, 

have the superceding before the the user exclusion. onlz dispplay top ranked treatment. then loop again if rejected.
onlz have eligibility and exclusion / severitz is eligibility
simple dosing strategy


Version 4

1. Changed the data structure from "exclusion" and "severity" as seperate lists, into a dictionary called "eligibility". Add post-coordination as a aligibility. 
2. Have the superceding before the the user exclusion. only display top ranked treatment. The user exclusion wil only be the top ranked treatments being displayed. IF they reject the treatment THEN the whole treatment evaluation process will be looped, until either the user accepts a treatment. OR there are no more treatments available. - each time the user rejects a tretment it enters a rejection list which is used as a filter the next loop. 
3. Instead of "diagnosis" and "comobidity" there is now diagnosis, and additional diseases added. All the treatments are stored ina  dictionary - before it was two seperate lists. - allows for a more flexible approach. 
- This will move the user acceptance of the treatment plan from before the drug is calculated to before that to after the superceding rules. 
Fixes: 
- added the recommended dictionary to be returned by the rules function
- allow you to add more than one treatment for rejection at once. 
- loop ends when no more treatments found 

to be done:

- change the dosing strategies from "neonate" etc, into the "dosing strategies" e.g. anti-biotic peak strategy, > 50's strategy. 
- key changes - data structure, dosing strategies, post-coordination,
- notify user that treatments exhausted for one disease, but continue search for other. 
# TreatmentRegimenCDSS
Thesis topic on dynamically selecting treatment regimens for clinicians.
None of the example drugs and examples are accurate and are just placeholders. 

1st iteration - rudimentary application of filters and exclusion criteria, with no rules for superceeding. Run main() in 1st iteration

Core funtions: filtering, ranking, user_exclusion, treaments as instances. 

Version 2 - use superceding.py to run from treatment evaluation process to the superceding process. It will take the IDs of the top ranking treatments, then run them against the superceding_rules_db rules, if non-are matched then the both the top treatments will print. If there is a match
then only the superceeding treatment will match. Will refactor code once the core process has been done - run superceding.py.

Core functions: filtering, ranking, user_exclusion, treatments in db, superceding rules and db.  The ranking is also dealt with using the CPG guideline that the user can select. This will indicate to the system which CPG ranking should be used. 
1. Primary filter applied using the disease from the user input.
2. Eligiblity criteria: exclusion and severity filters applied.
3. Ranking of treatments based on CPG.
4. User exclusion
5. Treatments re-ranked after the user exclusion.
6. Superseding rules applied.
7. Top treatments printed or treatment if rules are applied.

Version 3

1. Validation for treatment
2. Dosing function added - strategies are based on "standard", "child" , "neonate" that determine the dose. 
3. Takes weight as a parameter to be used in the calculation. 

Version 4

1. Changed the data structure from "exclusion" and "severity" as seperate lists, into a dictionary called "eligibility". Add post-coordination as a aligibility. 
2. Have the superceding before the the user exclusion. only display top ranked treatment. The user exclusion wil only be the top ranked treatments being displayed. IF they reject the treatment THEN the whole treatment evaluation process will be looped, until either the user accepts a treatment. OR there are no more treatments available. - each time the user rejects a tretment it enters a rejection list which is used as a filter the next loop. 
3. Instead of "diagnosis" and "comobidity" there is now diagnosis, and additional diseases added. All the treatments are stored ina  dictionary - before it was two seperate lists. - allows for a more flexible approach. 
- This will move the user acceptance of the treatment plan from before the drug is calculated to before that to after the superceding rules. 

to be done:

- change the dosing strategies from "neonate" etc, into the "dosing strategies" e.g. anti-biotic peak strategy, > 50's strategy. 
- key changes - data structure, dosing strategies, post-coordination,






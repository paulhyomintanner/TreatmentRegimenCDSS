# TreatmentRegimenCDSS
Thesis topic on dynamically selecting treatment regimens for clinicians.
None of the example drugs and examples are accurate and are just placeholders. 

1st iteration - rudimentary application of filters and exclusion criteria, with no rules for superceeding. Run main() in 1st iteration

Core funtions: filtering, ranking, user_exclusion, treaments as instances. 

Current version - use superceding.py to run from treatment evaluation process to the superceding process. It will take the IDs of the top ranking treatments, then run them against the superceding_rules_db rules, if non-are matched then the both the top treatments will print. If there is a match
then only the superceeding treatment will match. Will refactor code once the core process has been done - run superceding.py.

Core functions: filtering, ranking, user_exclusion, treatments in db, superceding rules and db.  The ranking is also dealt with using the CPG guideline that the user can select. This will indicate to the system which CPG ranking should be used. 
1. Primary filter applied using the disease from the user input.
2. Eligiblity criteria: exclusion and severity filters applied.
3. Ranking of treatments based on CPG.
4. User exclusion
5. Treatments re-ranked after the user exclusion.
6. Superseding rules applied.
7. Top treatments printed or treatment if rules are applied.
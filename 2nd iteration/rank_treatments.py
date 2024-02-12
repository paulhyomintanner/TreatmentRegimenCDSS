def rank_treatments(treatments, preferred_cpg):
    treatments.sort(key=lambda x: x['rank'][0][preferred_cpg])
    return treatments

#ranking function that uses teh CPG that is defined by the user to rank the treatments in a list. 

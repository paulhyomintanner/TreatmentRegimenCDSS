def rank_treatments(treatments, preferred_cpg):
    treatments.sort(key=lambda x: x['rank'][0][preferred_cpg])
    return treatments
#should just sort the list instead of sorting and returning a new list. 
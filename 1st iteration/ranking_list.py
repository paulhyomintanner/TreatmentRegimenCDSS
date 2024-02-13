def rank_treatments(filtered_treatments):
    filtered_treatments.sort(key=lambda treatment: treatment.rank)
    return filtered_treatments

#sorts the list of treatments based off their ranking. 
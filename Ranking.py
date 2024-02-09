def rank_treatments(filtered_treatments):
    # Sort the treatments based on their rank
    ranked_treatments = sorted(filtered_treatments, key=lambda treatment: treatment.rank)
    return ranked_treatments

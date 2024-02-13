def remove_treatments(treatments):
    while True:
        for i, treatment in enumerate(treatments):
            print(f"{i}: Name: {treatment.name}, Drugs: {', '.join(treatment.drugs)}")

        index_to_remove = input("Enter the index of the treatment to remove (or 'None' to finish): ")

        if index_to_remove.lower() == 'none':
            break

        index_to_remove = int(index_to_remove)
        if 0 <= index_to_remove < len(treatments):
            removed_treatment = treatments.pop(index_to_remove)
            print(f"Removed treatment: Name: {removed_treatment.name}, Drugs: {', '.join(removed_treatment.drugs)}")

    return treatments
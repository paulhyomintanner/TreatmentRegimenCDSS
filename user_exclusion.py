def remove_treatments(treatments):
    while True:
        # Print treatments with indices
        for i, treatment in enumerate(treatments):
            print(f"{i}: Name: {treatment.name}, Drugs: {', '.join(treatment.drugs)}")

        # Prompt the user to enter the index of the treatment to remove
        index_to_remove = input("Enter the index of the treatment to remove (or 'None' to finish): ")

        # If the user entered 'None', stop the removal process
        if index_to_remove.lower() == 'none':
            break

        # If the user entered a valid index, remove the treatment
        index_to_remove = int(index_to_remove)
        if 0 <= index_to_remove < len(treatments):
            removed_treatment = treatments.pop(index_to_remove)
            print(f"Removed treatment: Name: {removed_treatment.name}, Drugs: {', '.join(removed_treatment.drugs)}")

    return treatments
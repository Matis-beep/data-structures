def linear_search(roll_numbers, target_roll):
    for i in range(len(roll_numbers)):
        if roll_numbers[i] == target_roll:
            return i  
    return -1  



roll_numbers = [101, 105, 110, 115, 120, 125]


target_roll = int(input("Enter roll number to search: "))


result = linear_search(roll_numbers, target_roll)


if result != -1:
    print(f"Roll number {target_roll} found at position {result + 1}.")
else:
    print(f"Roll number {target_roll} not found in the list.")
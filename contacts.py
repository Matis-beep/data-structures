contacts = ["Alice", "Bob", "Charlie", "David", "Eve"]


user_input = input("Who are you looking for? ")


found = False

for i in range(len(contacts)):
    if contacts[i] == user_input:
        print(f"Found {user_input} at index {i}")
        found = True
        break


if not found:
    print("Contact not found")
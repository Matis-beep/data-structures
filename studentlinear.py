students =["Nameerah","Mathis","Ava","Alex","Amelie"]
target = input("Enter name for search:")

found = False

for name in students:
    if name == target:
        print("student found")
        found =True
        break

if not found:
    print("student not found!!")
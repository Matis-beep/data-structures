class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    # Getter
    def get_marks(self):
        return self.marks
    # Setter
    def set_marks(self, new_marks):
        self.marks = new_marks

# Taking input from user
name = input("Enter student name: ")
marks = int(input("Enter marks: "))
# Create object
student1 = Student(name, marks)
# Get marks
print("Current marks:", student1.get_marks())
# Update marks
new_marks = int(input("Enter updated marks: "))
student1.set_marks(new_marks)
# Get updated marks
print("Updated marks:", student1.get_marks())
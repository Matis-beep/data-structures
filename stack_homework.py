MAX = 10
stack = []

def push():
    if len(stack) >= MAX:
        print("Stack Overflow! Cannot push more elements.")
    else:
        element = input("Enter element to push: ")
        stack.append(element)
        print(element, "pushed into stack")

def pop():
    if len(stack) == 0:
        print("Stack Underflow! Stack is empty.")
    else:
        removed = stack.pop()
        print("Popped element:", removed)

def top():
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print("Top element:", stack[-1])

def size():
    print("Size of stack:", len(stack))


while True:
    print("\nStack Operations Menu")
    print("1. Push")
    print("2. Pop")
    print("3. Top")
    print("4. Size")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        top()
    elif choice == 4:
        size()
    elif choice == 5:
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Try again.")
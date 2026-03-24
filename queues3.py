
def is_balanced(expression):
    stack = []

   
    matching = {')': '(', '}': '{', ']': '['}

    for char in expression:
       
        if char in "({[":
            stack.append(char)

        
        elif char in ")}]":
            if not stack:
                return False
            top = stack.pop()
            if matching[char] != top:
                return False

    
    return len(stack) == 0



balanced = "{[()()]}"
unbalanced = "{[(])}"


print("Expression:", balanced)
print("Is Balanced?", is_balanced(balanced))

print("Expression:", unbalanced)
print("Is Balanced?", is_balanced(unbalanced))
def find_maximum(root):
    if root is None:
        return None
    
    while root.right is not None:
        root = root.right
    
    return root.data


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.right.right = Node(30)

print(find_maximum(root)) 
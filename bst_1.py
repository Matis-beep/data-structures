class TreeNode:
    def __init__(self,x):
        self.data=x
        self.leftchild=None
        self.rightchild=None
def inordertraversal(root):
    if root is not None:
        if root.leftchild is not None:
            inordertraversal(root.leftchild)
        print(root.data)
    
    if root.rightchild is not None:
        inordertraversal(root.rightchild)

def insert(root, k):
    if root == None:
        return TreeNode(k)
    
    if root.data > k:
        root.leftchild = insert(root.leftchild, k)
        
    else:
        root.rightchild = insert(root.rightchild, k)
        
    return root

def Search(root, key):
    if root.data == key:
        return root
    elif root.data > key and root.leftchild is not None:
        return Search(root.leftchild, key)
    
    elif root.data < key and root.rightchild is not None:
        return Search(root.rightchild, key)
    else:
        return -1

n = int(input("Enter the number of elements you want in the tree - "))
root = None
for i in range(n):
    x = int(input("Enter the node value - "))
    root = insert(root, x)

inordertraversal(root)
key = int(input("Enter the key to be searched - "))
keyNode = Search(root, key)

if keyNode == -1:
    print("Key does not exist in the tree")
else:
    print("Key exists", keyNode.data)
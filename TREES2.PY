class Node:
    def __init__(self,data):
        self.data=data
        self.left =None
        self.right=None
    
def insert(root,data):
        if root is None:
            return Node(data)
        queue=[root]

        while queue:
            temp=queue.pop(0)

            if temp.left is None:
                temp.left =Node(data)
                return root
            else:
                queue.append(temp.left)
            
            if temp.right is None:
                temp.right = Node(data)
                return root
            else:
                queue.append(temp.right)
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

root = None
while True:
    print("\n------ TREE MENU ------")
    print("1. Create Tree")
    print("2. Insert Node")
    print("3. Preorder Traversal")
    print("4. Inorder Traversal")
    print("5. Postorder Traversal")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        val = int(input("Enter root value: "))
        root = Node(val)
        print("Tree Created!")

    elif choice ==2:
        if root is None:
            print("Create a tree first!")
        else:
            val = int(input("Enter value to insert."))
            root = insert(root, val)
            print("Node Inserted.")
    elif choice == 3:
        if root is None:
            print("Tree is empty")
        else:
            print("Preorder: ", end = " ")
            preorder(root)
            print()
    elif choice == 4:
        if root is None:
            print("Tree is empty")
        else:
            print("Inorder: ", end = " ")
            inorder(root)
            print()

    elif choice == 5:
        if root is None:
            print("Tree is empty")
        else:
            print("Postorder: ", end = " ")
            postorder(root)
            print()

    elif choice == 6 :
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try Again!")
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftnode=None
        self.rightnode=None
def inordertraversal(root):
        if root.leftnode != None:
            inordertraversal(root.leftnode)
            print(root.data)
        if root.rightnode != None:
            inordertraversal(root.rightnode)
def preordertraversal(root):
     print(root.data)
     if root.leftnode != None:
        preordertraversal(root.leftnode)
     if root.rightnode != None:
          preordertraversal(root.rightnode)
def postordertraversal(root):
    if root.leftnode != None:
        postordertraversal(root.leftnode)
    if root.rightnode != None:
        postordertraversal(root.rightnode)
        print(root.data)

root=TreeNode(5)
root.leftnode=TreeNode(4)
root.leftnode.leftnode = TreeNode(2)

root.rightnode = TreeNode(8)
root.rightnode.leftnode = TreeNode(7)
root.rightnode.rightnode = TreeNode(9)

inordertraversal(root)
preordertraversal(root)
postordertraversal(root)
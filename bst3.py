class TreeNode:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

def is_bst(node, min_val, max_val):
    if node is None:
        return True
    
    if node.data <= min_val or node.data >= max_val:
        return False
    
    left_check = is_bst(node.left, min_val, node.data)
    right_check = is_bst(node.right, node.data, max_val)
    
    return left_check and right_check

def checkBST(root):
    return is_bst(root, float("-inf"), float("inf"))

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)

if checkBST(root):
    print("This is a valid BST.")
else:
    print("This is NOT a valid BST.")
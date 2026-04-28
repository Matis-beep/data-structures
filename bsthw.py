def findMaximum(root):
  
    if root is None:
        return None

   
    while root.right is not None:
        root = root.right

  
    return root.data
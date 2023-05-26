class TreeNode:
    
    def __init__(self,data):
        self.data = data
        self.children = []
        self. parent = None
    
    def add_child(self,child):
        self.child = child 
        child.parent = self
        self.children.append(child)
    
    

f = lambda n : n**2
root = TreeNode(f(5))
b = TreeNode(f(5))
print(b.data)

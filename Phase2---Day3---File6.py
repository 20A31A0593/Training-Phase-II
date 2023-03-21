# Adding an element in the Binary Search Tree

class Node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None
class BSTree:
    def add_element(self,root,value):
        new_node=Node(value) #step 1 create
        if new_node.data < root.data:
            if root.left!=None:
                self.add_element(root.left,value)
                return
            else:
                root.left = new_node
                return
        else:
            if root.right!=None:
                self.add_element(root.right,value)
                
            else:
                root.right=new_node
              

            
    def inorder(self,root):
        pass
    def preorder(self,root):
        pass
    def postorder(self,root):
        pass
    def levelorder(self,root):
        pass

ob=BSTree()
root=Node(10)
ob.add_element(root,7)
ob.add_element(root,40)
ob.add_element(root,5)
ob.add_element(root,9)
ob.add_element(root,15)
ob.add_element(root,60)

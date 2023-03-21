# To find height of a Binary Tree
class Node:
    def __init__(self, value):
        self.data=value
        self.left=None
        self.right=None
class BSTree:
    def add_element(self, root,  value):
        
        new_node=Node(value) #step 1 create
        if new_node.data < root.data:
            if root.left!=None:
                self.add_element(root.left, value)
                return
            else:
                root.left = new_node
                return
        else:
            if root.right!=None:
                self.add_element(root.right, value)
                
            else:
                root.right=new_node
       
        
    def inorder(self, root):
        pass
    def preorder(self, root):
        print(root.data , end=' ')
        
        if root.left!=None:
            self.preorder(root.left)
        

        if root.right!=None:
            self.preorder(root.right)
        
    def postorder(self, root):
        pass
    def levelorder(self, root):
        pass
    def search(self, root, value):
        pass
    def sum(self, root):
        pass
    
    def height(self, root):
        if root==None:
            return -1

        left_height=self.height(root.left)
        right_height=self.height(root.right)

        return 1+max(left_height,right_height)
        
        
ob=BSTree()
root=Node(10)
ob.add_element(root,4)
ob.add_element(root,15)
ob.add_element(root,2)
ob.add_element(root,5)
ob.add_element(root,7)

ob.preorder(root)
print()
print(ob.height(root))

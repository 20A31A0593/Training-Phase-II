# Adding an element in the Binary Search Tree according to inorder,preorder,postorder,level order
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

        if root.left!=None:
            self.inorder(root.left)
        print(root.data , end=' -> ')

        if root.right!=None:
            self.inorder(root.right)
        
    def preorder(self, root):

        print(root.data , end=' -> ')
        
        if root.left!=None:
            self.preorder(root.left)
        

        if root.right!=None:
            self.preorder(root.right)
        
    def postorder(self, root):
       
        if root.left!=None:
            self.postorder(root.left)
        

        if root.right!=None:
            self.postorder(root.right)
        
        print(root.data , end=' -> ')

        

    def levelorder(self, root): #use queue for levelorder
        q=[]
        q.append(root)
        while len(q) !=0:
            ele=q.pop(0)
            print(ele.data, end=' -> ')
            if ele.left:
                q.append(ele.left)
            
            if ele.right:
                q.append(ele.right)

            
            
          

ob=BSTree()
root=Node(10)
ob.add_element(root,7)
ob.add_element(root,40)
ob.add_element(root,5)
ob.add_element(root,9)
ob.add_element(root,15)
ob.add_element(root,60)
ob.inorder(root)
print()
ob.preorder(root)
print()
ob.postorder(root)
print()
ob.levelorder(root)
print()

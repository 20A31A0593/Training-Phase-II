#Insertion at a specified position in the list

class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class LinkedList():
    def add_ele_at_start(self,head,value):
        new_node=Node(value)
        new_node.next=head
        head=new_node
        return head
    def add_element(self,head,value):
        new_node=Node(value)
        temp=head
        while temp.next!=None:
            temp=temp.next
        temp.next=new_node
    def remove_element(self):
        temp=head
        while(temp.next.next!=None):
            temp=temp.next
        temp.next=None
    def print_list(self,head):
        temp=head
        while(temp!=None):
            print(temp.data,end=" -> ")
            temp=temp.next
    def search_element(self,value):
        pass
    def insert(self,head,value,pos):
        new_node=Node(value)
        current_node=head
        prev_node=None
        while(pos!=0):
            prev_node=current_node
            current_node=current_node.next
            pos-=1
        prev_node.next=new_node
        new_node.next=current_node
obj=LinkedList()
head=Node(10)
obj.add_element(head,20)
obj.add_element(head,30)
obj.add_element(head,40)
obj.add_element(head,50)
obj.add_element(head,60)
obj.insert(head,input(),2)
obj.print_list(head)
obj.remove_element()
print()
obj.print_list(head)

#Implementation of Linked Lists

class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class LinkedList():
    def add_element(self,head,value):
        new_node=Node(value)
        temp=head
        while temp.next!=None:
            temp=temp.next
        temp.next=new_node
    def remove_element(self):
        pass
    def print_list(self,head):
        temp=head
        while(temp!=None):
            print(temp.data)
            temp=temp.next
    def search_element(self,value):
        pass
obj=LinkedList()
head=Node(10)
obj.add_element(head,20)
obj.add_element(head,30)
obj.add_element(head,40)
obj.add_element(head,50)
obj.add_element(head,60)
obj.print_list(head)


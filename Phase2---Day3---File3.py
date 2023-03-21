#Implementation of Double Linked Lists

class Node:
    def __init__(self,value):
        self.prev=None
        self.data=value
        self.next=None
class DoubleLinkedList():
    def add_element(self,head,value):
        new_node=Node(value)
        temp=head
        while temp.next!=None:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp
    def remove_element(self):
        temp=head
        while(temp.next.next!=None):
            temp=temp.next
        temp.next.prev=None
        temp.next=None
    def print_list(self,head):
        temp=head
        while(temp!=None):
            print(temp.data,end=" -> ")
            temp=temp.next
        print()
    def print_reverse(self,head):
        temp=head
        while(temp.next!=None):
            temp=temp.next
        while temp:
            print(' <-',temp.data,end="")
            temp=temp.prev
        print()
    def search_element(self,value):
        pass
obj=DoubleLinkedList()
head=Node(10)
obj.add_element(head,20)
obj.add_element(head,30)
obj.add_element(head,40)
obj.add_element(head,50)
obj.add_element(head,60)
obj.print_list(head)
obj.print_reverse(head)


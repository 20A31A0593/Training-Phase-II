#Flower Shop

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
        temp=head
        while(temp.next.next!=None):
            temp=temp.next
        temp.next=None
    def print_list(self,head):
        temp=head
        while(temp!=None):
            print(temp.data,end=" -> ")
            temp=temp.next
obj1=LinkedList()
obj2=LinkedList()
n=int(input("Enter the no. of different types of flowers:"))
print("Enter the flowers and the their count:")
head1=None
head2=None
for i in range(n):
    str=input().split(" ")
    if(i==0):
        head1=Node(str[1])
        head2=Node(str[2])
    else:
        obj1.add_element(head1,str[1])
        obj2.add_element(head2,str[2])
#obj1.print_list(head1)
#print()
#obj2.print_list(head2)
q=int(input("Enter the no. of queries:"))
for i in range(q):
    s=input().split(" ")


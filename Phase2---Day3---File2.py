#Reversing second half of the linked list

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
    def reverse(self,head,n):
        curr=head
        prev=None
        i=0
        x=None
        while(i<n):
            if(i<(n//2)):
                x=curr
                curr=curr.next
            elif(i>=(n//2)):
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            i+=1
        x.next=prev
        return head
obj=LinkedList()
n=int(input("Enter the no. of elements to be inserted:"))
print("Enter the elements to be inserted:")
head=None
for i in range(n):
    if(i==0):
        head=Node(input())
    else:
        obj.add_element(head,input())
obj.print_list(head)
#ele=input("\nEnter the element to be inserted:")
#pos=int(input("Enter the position at which the element must be inserted:"))
#obj.insert(head,ele,pos)
#print()
#obj.print_list(head)
head=obj.reverse(head,n)
print()
obj.print_list(head)

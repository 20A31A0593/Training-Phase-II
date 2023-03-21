#Finding prime numbers in the linked list

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
        x=head
        curr=head
        prev=None
        while(n!=0):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
            n-=1
        x.next=curr
        return prev
    def prime(self,head):
        temp=head
        while(temp!=None):
            count=0
            for i in range(2,(temp.data//2)+1):
                if(temp.data%i==0):
                    count+=1
                    break
            if(count==0 and temp.data!=1 and temp.data!=0):
                print(temp.data,end=" ")
            temp=temp.next
obj=LinkedList()
n=int(input("Enter the no. of elements to be inserted:"))
print("Enter the elements to be inserted:")
head=None
for i in range(n):
    if(i==0):
        head=Node(int(input()))
    else:
        obj.add_element(head,int(input()))
obj.print_list(head)
print()
print("The prime numbers in the list are:")
obj.prime(head)

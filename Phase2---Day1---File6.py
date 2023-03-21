#Implementing the functionality of Stack using Queue


class Queue:
    def _init_(self):
        self.temp=[]
        self.original=[]
    def enqueue(self,element):
        self.temp.append(element)     #step 1
        while len(self.original)!=0:   #step 2
            pop_element=self.original.pop(0)
            self.temp.append(pop_element)
        while len(self.temp)!=0:#step 3
            pop_element=self.temp.pop(0)
            self.original.append(pop_element)

    def dequeue(self):
        return self.original.pop(0)
    def printQueue(self):
        print("Temp:",self.temp)
        print("Original:",self.original)

ob= Queue()
ob.enqueue(10)
ob.enqueue(20)
ob.enqueue(30)
ob.enqueue(40)
ob.enqueue(50)
ob.printQueue()

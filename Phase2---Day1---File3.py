class Queue:
    arr=[]
    size=5
    def enqueue(self,element):
        if(len(self.arr)==self.size):
            print("Queue Overflow")
        else:
            self.arr.append(element)
    def dequeue(self):
        if(len(self.arr)==0):
            print("Queue Underflow")
        else:
            print(self.arr.pop(0))
    def isEmpty(self):
        if(len(self.arr)==0):
            return True
        else:
            return False
q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
q.enqueue(10)
q.dequeue(10)
q.dequeue(20)
q.dequeue(30)
q.dequeue(40)
q.dequeue(50)

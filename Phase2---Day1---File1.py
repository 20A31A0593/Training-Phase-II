class Stack:
    arr=[]
    size=5
    def stack_push(self,element):
        if(len(self.arr)==self.size):
            print("Stack Overflow")
        else:
            self.arr.append(element)
    def stack_pop(self):
        if(len(self.arr)==0):
            print("Stack Underflow")
        else:
            self.arr.pop()
    def stack_peek(self):
        if(len(self.arr)==0):
            print("Stack is Empty")
        else:
            return self.arr[-1]
    def isEmpty(self):
        if(len(self.arr)==0):
            return True
        else:
            return False
s=Stack()
s.stack_push(10)
s.stack_push(20)
s.stack_push(30)
s.stack_push(40)
s.stack_push(50)
s.stack_push(60)
print(s.arr)
s.stack_pop()
s.stack_pop()
s.stack_pop()
s.stack_pop()
s.stack_pop()
s.stack_pop()
print(s.arr)
print(s.stack_peek())

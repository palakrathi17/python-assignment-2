class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
            self.stack.append(item)
    def pop(self):
        if self.stack!=[]:
            self.stack.pop()
        else:
            print("stack is empty")
    def peek(self):
        if self.stack!=[]:
            print(self.stack[-1])
        else:
            print("stack empty")
    def display(self):
        print(self.stack)
s=Stack()
s.push(22)
s.push(12)
s.pop()
s.display()
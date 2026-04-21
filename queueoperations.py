class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        if self.queue==[]:
            print("queue empty")
        else:
            self.queue.pop(0)
    def peek(self):
        if self.queue==[]:
            print("queue empty")
        else:
            print(self.queue[0])
    def display(self):
        print(self.queue)
q=Queue()
q.enqueue(10)
q.enqueue(19)
q.enqueue(25)
q.dequeue()
q.peek()
q.display()




        
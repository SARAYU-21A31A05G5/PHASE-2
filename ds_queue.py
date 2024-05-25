class queue:
    def __init__(self,s):
        self.size=s
        self.q=[]
        self.front=self.rear=-1
    def enqueue(self,d):
        if self.rear<self.size-1:
            self.q.append(d)
            if self.front==-1:
                # self.q.append(d)
                self.front=self.rear=0
            else:
                # self.q.append(d)
                self.rear+=1
        else:
            print("Queue is full !")
    def dequeue(self):
            if self.rear==-1 or self.rear<self.front:
                print("Queue is empty")
            else:
                # self.q.pop(self.front)
                self.front+=1
    def display(self):
        if self.q!=[]:
            for i in range(self.front,self.rear+1):
                print(self.q[i])
p=queue(int(input("Enter the size of the queue:")))
p.enqueue(31)
p.enqueue(100)
p.enqueue(56)
p.enqueue(25)
p.dequeue()
# p.display()
p.dequeue()
p.dequeue()
p.dequeue()
p.display()
p.display()
        
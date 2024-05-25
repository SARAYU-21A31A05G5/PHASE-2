class Stack:
    def __init__(self,s):
        self.st=[]
        self.size=s
        self.top=-1
    def push(self,d):
        if self.top<self.size-1:
            self.st.append(d)
            self.top+=1
        else:
            print("Stack is overflow !")
    def pop(self):
        if self.top==-1:
            print("Stack is underflow !")
        else:
            self.st.pop()
            self.top-=1
    def peek(self):
        print(self.st[self.top])
    def display(self):
        print(self.st)
ob=Stack(int(input("Enter the size of the stack :")))
ob.push(9)
ob.push(8)
ob.push(12)
ob.pop()
ob.peek()
ob.display()
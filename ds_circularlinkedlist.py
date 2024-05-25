class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Cll:
    def __init__(self):
        self.head=None
    def inser_beg(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            self.head.next=newNode
            return
        current=self.head
        while current.next!=self.head:
            current=current.next
        newNode.next=self.head
        current.next=newNode
        self.head=newNode
    def insert_end(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            self.head.next=newNode
            return
        current=self.head
        while current.next!=self.head:
            current=current.next
        newNode.next=self.head
        current.next=newNode
    def delete_beg(self):
        if self.head is None:
            print("Circular Linked List is empty")
            return
        current=self.head
        while current.next!=self.head:
            current=current.next
        self.head=self.head.next
        current.next=self.head
    def delete_end(self):
        if self.head is None:
            print("Circular Linked List is empty")
            return
        current=self.head
        while current.next.next!=self.head:
            current=current.next
        current.next=self.head
    def delete_value(self,value):
        if self.head is None:
            print("Circular Linked List is empty")
            return
        current=self.head
        while current.next!=self.head:
            
    def display(self):
        print(self.head.data,end="->")
        current=self.head.next
        while current!=self.head:
            print(current.data,end="->")
            current=current.next
obj=Cll()
obj.inser_beg(9)
obj.inser_beg(20)
obj.insert_end(50)
obj.delete_end()
obj.display()
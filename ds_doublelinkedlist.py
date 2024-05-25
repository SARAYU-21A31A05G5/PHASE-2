class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoubleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert_beg(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=self.tail=newNode
        else:
            newNode.next=self.head
            newNode.next.prev=newNode #self.head.prev=newNode
            self.head=newNode
    def insert_end(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=self.tail=newNode
        else:
            newNode.prev=self.tail
            self.tail.next=newNode #newNode.prev.next=newNode
            self.tail=newNode
    def insert_pos(self,pos,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        elif pos==1:
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode
        else:
            current=self.head
            count=0
            while current:
                count+=1
                if count==pos-1:
                    newNode.next=current.next.prev
                    newNode.prev=current.next
                    current.next=newNode
                    current.next.prev=newNode
                    break
                current=current.next
    def delete_beg(self):
        if self.head is None:
            print("Double Linked List is empty ")
        elif self.head==self.tail:
            self.head=self.tail=None
        else:
            self.head.next.prev=None
            self.head=self.head.next
    def delete_end(self):
        if self.head is None:
            print("Double Linked List is empty")
        elif self.head==self.tail:
            self.head=self.tail=None
        else:
            self.tail=self.tail.prev
            self.tail.next=None
    def delete_value(self,value):
        if self.head is None:
            print("Double Linked List is empty")
        elif self.head.data==value:
            self.delete_beg()
        elif self.tail.data==value:
            self.delete_end()
        else:
            current=self.head
            while current.next:
                if current.data==value:
                    current.prev.next=current.next
                    current.next.prev=current.prev
                current=current.next
    def delete_pos(self,pos):
        if self.head is None:
            print("Double linked list is empty")
        elif pos==1:
            self.delete_beg()
        else:
            count=0
            current=self.head
            while current.next:
                count+=1
                if count==pos:
                    current.prev.next=current.next
                    current.next.prev=current.prev
                current=current.next
            if count<pos:
                self.delete_end()
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            current=self.head
            print("The double linked list is: ",end="")
            while current:
                print(current.data,end="<->")
                current=current.next
            print()
    def rev_display(self):
        if self.head is None:
            print("Double Linked List is empty !")
        else:
            current=self.tail
            print("The reverse double linked list is: ",end="")
            while current:
                print(current.data,end="<->")
                current=current.prev
            print()
obj=DoubleLinkedList()
obj.insert_beg(int(input()))
obj.insert_beg(int(input()))
obj.insert_end(int(input()))
obj.insert_end(int(input()))
obj.insert_beg(int(input()))
# obj.insert_pos(2,4)
obj.delete_pos(5)
# obj.delete_beg()
# obj.delete_end()
obj.display()
# obj.rev_display()
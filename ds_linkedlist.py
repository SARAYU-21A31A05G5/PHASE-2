class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_beg(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode
    def insert_end(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=newNode
    def insert_pos(self,pos,value):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
        elif pos==0:
            newNode=self.head
            self.head=newNode
        else:
            current=self.head
            count=0
            while current:
                count+=1
                if count!=pos:
                    current=current.next
                else:
                    newNode.next=current.next
                    current.next=newNode
    def delete_beg(self):
        if self.head is None:
            print("Linked list is empty !")
        else:
            current=self.head.next
            self.head=current
    def delete_end(self):
        if self.head is None:
            print("Linked list is empty !")
        if self.head.next is None:
            self.head=None
            return self.delete_end()
        else:
            current=self.head
            while current.next.next:
                current=current.next
            current.next=None
    def delete_value(self,value):
        if self.head is None:
            print("Linked List is empty!")
        if self.head.data==value:
            self.head=self.head.next
        else:
            current=self.head
            while current.next and current.next.data!=value:
                    current=current.next
            if current.next is None:
                print("No data found")
                # return
            else:
                current.next=current.next.next
    # def mid(self):
    #     current=self.head
    #     count=0
    #     while current:
    #         count+=1
    #         current=current.next
    #     print(count)
    #     if count%2==0:
    #         count=count/2
    #     else:
    #         count=1+count//2
    #     print(count)
    #     current=self.head
    #     i=1
    #     while i!=count:
    #         current=current.next
    #         i=i+1
    #     print(current.data)
    def mid(self):
        c1=c2=self.head
        while c2.next and c2.next.next:
            c1=c1.next
            c2=c2.next.next
        print(f"Mid valuue is :{c1.data}")

    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
    def rev_display(self):
        prev=None
        current=self.head
        next=None
        while current:
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev
        self.display()
    def find(self,data):
        current=self.head
        count=0
        while current:
            if current.data!=data:
                current=current.next
                count+=1
            else:
                print("data found at",count)
                break
    def min(self):
        m=10000
        current=self.head
        while current:
            if current.data<m:
                m=current.data
                current=current.next
            else:   
                current=current.next
        print(m)
    def max(self):
        m=0
        current=self.head
        while current:
            if current.data>m:
                m=current.data
                current=current.next
            else:
                current=current.next
        print(m)
        
obj=LinkedList()
obj.insert_beg(5)
obj.insert_beg(7)
obj.insert_beg(3)
obj.insert_end(11)
obj.max()
obj.min()
# obj.mid()
# obj.insert_pos(5,46)
# obj.delete_value(7)
# obj.delete_end()
# obj.display()
# n=int(input("Enter the element to be found"))
# obj.find(n)
# obj.rev_display()
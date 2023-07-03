class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedLists:
    def __init__(self):
        self.head=None
    def push(self,data):
        New_node=node(data)
        if self.head==None:
            self.head=New_node
            return
        New_node.data=data
        New_node.next=self.head
        self.head=New_node
    def display(self):
        current=self.head
        while(current!=None):
            print(current.data , end=" ->")
            current=current.next
        print("null")
    def iterateReverse(self):
        if self.head==None or self.head.next==None:
            return

        current=self.head.next
        prev=self.head
        while(current!=None):
            NextNo=current.next
            current.next=prev
            prev=current
            current=NextNo

        self.head.next=None
        self.head=prev

if __name__=="__main__":
    ll=LinkedLists()
    ll.push(5)
    ll.push(6)
    ll.push(7)
    ll.push(8)
    ll.push(9)
    ll.push(10)
    ll.display()
    ll.iterateReverse()
    ll.display()

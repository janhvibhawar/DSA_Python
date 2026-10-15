class Node:
    def __init__(self,val):
        self.prev=None
        self.data=val
        self.next=None

    
class LinkedList:
    def __init__(self):        
        self.head=None

    def append(self,new_node):
        temp=self.head
        if temp:
            while temp.next:
                temp=temp.next
            temp.next=new_node
            new_node.prev=temp
        else:
            self.head=new_node

    def insert(self,new_node,pos):
        temp=self.head
        if pos==1:
            new_node.next=self.head
            self.head.prev = new_node
            self.head=new_node
        else:
            p=1
            while(p!=pos-1 and temp.next):
                temp=temp.next
                p+=1
            new_node.next = temp.next
            if temp.next:   #for last position
                temp.next.prev = new_node
            temp.next = new_node
            new_node.prev = temp



    def print(self):
        temp=self.head
        print("List elements:")
        while temp:
            print(temp.data, end=" ")
            temp=temp.next
        print()


list=LinkedList()
n1=Node(10)
n2=Node(20)
n3=Node(30)

list.append(n1)
list.append(n2)
list.append(n3)

list.append(Node(40))
list.print()            
list.insert(Node(70),5)
list.print()


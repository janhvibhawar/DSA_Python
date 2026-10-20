class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self,new_node):
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = new_node
            

    def insert(self,new_node,pos):
        if pos==1:
            new_node.next = self.head
            self.head = new_node

        else:
            temp=self.head
            p = 1
            while p!=pos-1 and temp is not None:
                temp = temp.next
                p+=1

            if temp is not None:
                new_node.next = temp.next
                temp.next = new_node
            else:
                print("Position is not valid")

    def print(self):
        temp = self.head
        while(temp):
            print(temp.data, end = "->")
            temp = temp.next
        print("None")

list = Linkedlist()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

list.append(n1)
list.append(n2)
list.append(n3)
list.append(n4)

list.insert(n5,3)

list.print()


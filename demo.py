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

    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end = "->")
            temp = temp.next
        print("None")

list = Linkedlist()

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

list.append(node1)
list.append(node2)
list.append(node3)
list.append(node4)

list.print()
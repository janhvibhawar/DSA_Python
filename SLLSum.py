class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if(self.head == None):
            self.head = new_node
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = new_node
    
    def print(self):
        sum = 0
        temp = self.head
        while temp:
            print(temp.data)
            sum+=temp.data
            temp = temp.next
        print("Sum of nodes:", sum)


list = LinkedList()
n1 = Node(20)
n2 = Node(30)
n3 = Node(50)

list.append(n1)
list.append(n2)
list.append(n3)

list.append(Node(60))
list.print()
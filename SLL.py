#~Singlly Linear Linked list
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None
    def append(self, new_node):
        if (self.head == None):
            self.head = new_node
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = new_node
    def print(self):
        cnt = 0
        sum = 0
        temp = self.head
        while temp:
            print(temp.data)
            cnt+=1
            sum+=temp.data
            temp = temp.next
        print("Number of nodes:", cnt)
        print("Sum of all nodes:", sum)

list = Linkedlist()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
list.append(n1)
list.append(n2)
list.append(n3)

list.append(Node(40))
list.print()
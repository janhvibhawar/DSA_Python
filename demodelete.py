class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    
    def insert(self,new_node,pos):
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            p = 1
            while p!=pos-1 and temp is not None:
                temp = temp.next
                p+=1
            if temp is not None:
                new_node.next = temp.next
                temp.next = new_node
            else:
                print("Position invalid")

    def delete(self,val):
        temp = self.head
        if temp.data == val:
            self.head=self.head.next
            return

        prev = None
        temp = self.head

        while temp is not None:
            if(temp.data == val):
                break
            prev = temp
            temp = temp.next

        if temp is None:
            print("List is empty")
            return

        prev.next = temp.next

    
    def print(self):
        temp = self.head
        while(temp):
            print(temp.data, end="->")
            temp = temp.next
        print("None")

list = LinkedList()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

list.append(n1)
list.append(n2)
list.append(n3)
list.append(n4)

n5 = Node(50)

list.insert(n5,5)
list.delete(40)

list.print()



class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, node):
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node

    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


    def concatenate(self,list2):
        if self.head is None:
            self.head = list2.head
            return
            
        temp=self.head
        while(temp.next):
            temp=temp.next
        temp.next=list2.head


list1 = LinkedList()
list2 = LinkedList()

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)

list1.append(n1)
list1.append(n2)
list1.append(n3)
list1.append(n4)
list1.append(n5)

n6 = Node(60)
n7 = Node(70)
n8 = Node(80)
n9 = Node(90)
n10 = Node(100)

list2.append(n6)
list2.append(n7)
list2.append(n8)
list2.append(n9)
list2.append(n10)


print("Original List:")
list1.print()

print("Second List")
list2.print()

list1.concatenate(list2)
print("Concatenated list:")
list1.print()
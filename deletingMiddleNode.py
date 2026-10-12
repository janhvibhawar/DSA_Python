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

    def reverse(self):
        prev = None
        temp = self.head

        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node

        self.head = prev

    def findmid_del(self):
        temp = temp1 = self.head
        prev = None

        if self.head is None:
            print("List is empty")
            return

        while temp1 and temp1.next:
            prev = temp
            temp = temp.next
            temp1 = temp1.next.next

        print("Middle Node:", temp.data)

        if prev is None:
            self.head = temp.next
        else:
            prev.next = temp.next


    def delfirst_last(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next.next is not None:
            temp = temp.next

        temp.next = None


    def delalternate_nodes(self):
        prev=self.head
        temp=self.head.next

        if self.head is None:
            print("List is empty")
            return

        while temp and prev:
            prev.next = temp.next
            temp=None #delete node
            prev = prev.next
            if prev:
                temp = prev.next


list1 = LinkedList()

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


print("Original List:")
list1.print()

print("Second List")
list2.print()

list1.findmid_del()
print("After deleting middle node:")
list1.print()

list1.reverse()
print("Reversed List:")
list1.print()

list1.delfirst_last()
print("After deleting first and last nodes:")
list1.print()

list1.delalternate_nodes()
print("After deleting alternate nodes:")
list1.print()

class Node:
    def __init__(self, val):
        self.prev = None
        self.data = val
        self.next = None

    
class LinkedList:
    def __init__(self):        
        self.head = None

    def append(self, new_node):
        temp = self.head
        if temp:
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        else:
            self.head = new_node

    def insert(self, new_node, pos):
        if pos == 1:
            new_node.next = self.head
            if self.head:  # Check if list is not empty
                self.head.prev = new_node
            self.head = new_node
        else:
            temp = self.head
            p = 1
            # Traverse until the position or the end of the list
            while p != pos - 1 and temp and temp.next:
                temp = temp.next
                p += 1
            
            if not temp: # Position is out of bounds
                return

            new_node.next = temp.next
            if temp.next:   # If inserting in the middle
                temp.next.prev = new_node
            temp.next = new_node
            new_node.prev = temp

    def reverse(self):
        temp = self.head
        if not temp:
            print("List is empty")
            return

        while temp.next:
            temp = temp.next
        
        print("List of elements in reverse:")
        while temp:
            print(temp.data, end=" ")
            temp = temp.prev
        print()

    def delete(self, value):
        temp = self.head
        if not temp:
            print("List is empty")
            return

        # Case 1: Deleting the head node
        if temp.data == value:
            self.head = self.head.next
            if self.head:  # If there is a next node, clear its prev pointer
                self.head.prev = None
            print(f"List of elements after deletion of {value}:")
            return

        # Case 2: Deleting middle or last node
        # Fixed: Check if temp exists BEFORE checking temp.data
        while temp and temp.data != value:
            temp = temp.next

        if temp is None:
            print(f"Value {value} is not present in the list")
            return

        print(f"List of elements after deletion of {value}:")
        temp.prev.next = temp.next
        if temp.next: # If it's not the last node
            temp.next.prev = temp.prev

    def count_occ(self,num):
        temp = self.head
        cnt = 0
        while temp:
            if temp.data==num:
                cnt+=1
            temp = temp.next
        print("The occurence of element", cnt)

    def swap(self):
        temp=node1=self.head #node1 is first node 

        while(temp.next): # temp is last node
            temp=temp.next

        temp.next = node1.next
        node1.next = None
        node1.prev = temp.prev
        temp.prev.next=node1
        temp.prev = None
        self.head = temp

    def print(self):
        temp = self.head
        print("List elements:")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Execution
list = LinkedList()
n1 = Node(10)
n2 = Node(10)
n3 = Node(30)

list.append(n1)
list.append(n2)
list.append(n3)

list.append(Node(40))
list.print()            

list.insert(Node(70), 5)
list.print()

list.delete(40)
list.print()

list.reverse()
list.swap()
list.print()
list.count_occ(10)



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # 1 Create Linked List
    def create(self):
        self.head = None
        n = int(input("Enter number of nodes: "))

        if n < 0:
            print("Number of nodes cannot be negative.")
            return

        for i in range(n):
            data = int(input("Enter node value: "))
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
            else:
                temp = self.head
                while temp.next is not None:
                    temp = temp.next
                temp.next = new_node

        print("Linked List created successfully.")

    # 2 Traverse and print
    def traverse(self):
        if self.head is None:
            print("Linked List is empty.")
            return

        temp = self.head
        print("Linked List:", end=" ")

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # 3 Insert node at a specific position
    def insert(self):
        data = int(input("Enter value to insert: "))
        pos = int(input("Enter position: "))

        if pos < 1:
            print("Invalid position.")
            return

        new_node = Node(data)

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            print("Node inserted successfully.")
            return

        temp = self.head

        for i in range(pos - 2):
            if temp is None:
                print("Invalid position.")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position.")
            return

        new_node.next = temp.next
        temp.next = new_node
        print("Node inserted successfully.")

    # 4 Find middle node
    def find_middle(self):
        if self.head is None:
            print("Linked List is empty.")
            return

        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        print("Middle node value:", slow.data)

    # 5 Delete node at a specific position
    def delete(self):
        if self.head is None:
            print("Linked List is empty.")
            return

        pos = int(input("Enter position to delete: "))

        if pos < 1:
            print("Invalid position.")
            return

        if pos == 1:
            self.head = self.head.next
            print("Node deleted successfully.")
            return

        temp = self.head

        for i in range(pos - 2):
            if temp is None:
                print("Invalid position.")
                return
            temp = temp.next

        if temp is None or temp.next is None:
            print("Invalid position.")
            return

        temp.next = temp.next.next
        print("Node deleted successfully.")

    # 6 Reverse Linked List
    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev
        print("Linked List reversed successfully.")

    # 7 Sum of consecutive node values
    def sum_consecutive(self):
        if self.head is None or self.head.next is None:
            print("At least two nodes are required.")
            return

        temp = self.head

        while temp.next is not None:
            total = temp.data + temp.next.data
            print(temp.data, "+", temp.next.data, "=", total)
            temp = temp.next



ll = SinglyLinkedList()

while True:
    print("\n--- SINGLY LINEAR LINKED LIST ---")
    print("1. Create Linked List")
    print("2. Traverse and Print")
    print("3. Insert Node")
    print("4. Find Middle Node")
    print("5. Delete Node")
    print("6. Reverse Linked List")
    print("7. Sum of Consecutive Nodes")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        ll.create()
    elif choice == 2:
        ll.traverse()
    elif choice == 3:
        ll.insert()
    elif choice == 4:
        ll.find_middle()
    elif choice == 5:
        ll.delete()
    elif choice == 6:
        ll.reverse()
    elif choice == 7:
        ll.sum_consecutive()
    elif choice == 8:
        print("Program terminated.")
        break
    else:
        print("Invalid choice. Please try again.")

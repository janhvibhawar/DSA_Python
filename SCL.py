class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

    
class LinkedList:
    def __init__(self):        
        self.head=None

    def append(self,new_node):
        if self.head==None:
            self.head=new_node
            new_node.next = self.head

        else:
            temp=self.head

            while(temp.next!=self.head):
                temp=temp.next
            temp.next=new_node 
            new_node.next=self.head

    def insert(self,new_node,pos):
         if pos==1:
            temp=self.head

            while(temp.next!=self.head): #find last node
                temp=temp.next

            new_node.next=self.head
            self.head=new_node
            temp.next=self.head

         else:#insert node from 2nd to last position
             p=1

             while(p!=pos-1):
                temp=temp.next
                p+=1
                
             new_node.next=temp.next
             temp.next=new_node 

    def delete(self, value):
        temp=None

    def print(self):
        print()
        print("List elements:")
        temp=self.head
        while (True):
            print(temp.data, end=" ")
            temp=temp.next
            if temp==self.head:
                break


list=LinkedList()
n1=Node(10)
n2=Node(20)
n3=Node(30)

list.append(n1)
list.append(n2)
list.append(n3)

list.append(Node(40))
list.print()            

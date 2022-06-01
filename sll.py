print("a. Creation")
print("b. Insertion")
print("c. Deletion")
print("d. Traversal")
while (True):
    choice = input("Select a choice:")
    if choice == "a":
        class Node:

            def __init__(self, data):
                self.data = data
                self.next = None

        class LinkedList:

            def __init__(self):
                self.head = None

            def printList(self):
                temp = self.head
                while (temp):
                    print(temp.data)
                    temp = temp.next

        if __name__ == '__main__':
            llist = LinkedList()

            print("Creation:")
            print("Input the items in the list")
            llist.head = Node(input("Enter:"))
            second = Node(input("Enter:"))
            third = Node(input("Enter:"))

            llist.head.next = second
            second.next = third
            print("The list:")
            llist.printList()
        break

    elif choice == "b":
        class Node:

            def __init__(self, data):
                self.data = data
                self.next = None

        class LinkedList:

            def __init__(self):
                self.head = None

            def printList(self):
                temp = self.head
                while (temp):
                    print(temp.data)
                    temp = temp.next

            def AtEnd(self, newdata):
                NewNode = Node(newdata)
                if self.head is None:
                    self.head = NewNode
                    return
                last = self.head
                while (last.next):
                    last = last.next
                last.next = NewNode

        if __name__ == '__main__':
            llist = LinkedList()

            print("Input the items in the list")
            llist.head = Node(input("Enter:"))
            second = Node(input("Enter:"))
            third = Node(input("Enter:"))

            llist.head.next = second
            second.next = third
            print("The list:")
            llist.printList()

            print("Insertion:")
            llist.AtEnd(input("Enter:"))
            print("The list after insertion at the end:")
            llist.printList()

            break

    elif choice == "c":
        class Node:

            def __init__(self, data):
                self.data = data
                self.next = None

        class LinkedList:

            def __init__(self):
                self.head = None

            def printList(self):
                temp = self.head
                while (temp):
                    print(temp.data)
                    temp = temp.next

            def RemoveNode(self, Removekey):
                HeadVal = self.head

                if (HeadVal is not None):
                    if (HeadVal.data == Removekey):
                        self.head = HeadVal.next
                        HeadVal = None
                        return
                while (HeadVal is not None):
                    if HeadVal.data == Removekey:
                        break
                    prev = HeadVal
                    HeadVal = HeadVal.next

                if (HeadVal == None):
                    return

                prev.next = HeadVal.next
                HeadVal = None

        if __name__ == '__main__':
            llist = LinkedList()

            print("Input the items in the list")
            llist.head = Node(input("Enter:"))
            second = Node(input("Enter:"))
            third = Node(input("Enter:"))

            llist.head.next = second
            second.next = third
            print("The list:")
            llist.printList()

            print("Deletion:")
            a = input("Enter the item to be deleted:")
            llist.RemoveNode(a)
            print("The new list")
            llist.printList()
        break
    elif choice == "d":

        class Node:
            def __init__(self, data):
                self.data = data
                self.next = None

        class SinglyLinkedList:
            def __init__(self):
                self.head = None
                self.tail = None

            def addNode(self, data):
                if self.tail is None:
                    self.head = Node(data)
                    self.tail = self.head
                else:
                    self.tail.next = Node(data)
                    self.tail = self.tail.next

            def display(self):
                current = self.head
                while current is not None:
                    print(current.data, end=' ')
                    current = current.next

        print("Traversal:")
        s = SinglyLinkedList()
        n = int(input('Enter the number of elements in linked list : '))
        for i in range(n):
            data = int(input('Enter data: '))
            s.addNode(data)
        print('The linked list: ', end='')
        s.display()
        break

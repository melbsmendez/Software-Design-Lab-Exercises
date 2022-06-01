print("a. Creation")
print("b. Insertion")
print("c. Deletion")
print("d. Traversal")
while(True):
    choice = input("Select a choice:")
    if choice == "a":
        class Node:
            def __init__(self, my_data):
                self.data = my_data
                self.next = None

        class circularLinkedList:
            def __init__(self):
                self.head = None

            def add_data(self, my_data):
                ptr = Node(my_data)
                temp = self.head
                ptr.next = self.head

                if self.head is not None:
                    while (temp.next != self.head):
                        temp = temp.next
                    temp.next = ptr
                else:
                    ptr.next = ptr
                self.head = ptr

            def print_it(self):
                temp = self.head
                if self.head is not None:
                    while (True):
                        print(temp.data),
                        temp = temp.next
                        if (temp == self.head):
                            break

        my_list = circularLinkedList()
        print("Creation:")
        my_list.add_data(input("Enter:"))
        my_list.add_data(input("Enter:"))
        my_list.add_data(input("Enter:"))
        my_list.add_data(input("Enter:"))
        print("The data is : ")
        my_list.print_it()

        break

    elif choice == "b":
        class Node:
            def __init__(self, data):
                self.data = data
                self.next = None

        class CreateList:

            def __init__(self):
                self.head = Node(None)
                self.tail = Node(None)
                self.head.next = self.tail
                self.tail.next = self.head

            def addAtEnd(self, data):
                newNode = Node(data)

                if self.head.data is None:
                    self.head = newNode
                    self.tail = newNode
                    newNode.next = self.head

                else:
                    self.tail.next = newNode
                    self.tail = newNode
                    self.tail.next = self.head

            def display(self):
                current = self.head

                if self.head is None:
                    print("List is empty")
                    return

                else:
                    print("Adding nodes to the end of the list: ")

                    print(current.data),
                    while (current.next != self.head):
                        current = current.next
                        print(current.data)

        class CircularLinkedList:
            print("Insertion:")
            cl = CreateList()
            cl.addAtEnd(input("Enter an item:"))
            cl.display()
            cl.addAtEnd(input("Enter an item:"))
            cl.display()
            cl.addAtEnd(input("Enter an item:"))
            cl.display()
            cl.addAtEnd(input("Enter an item:"))
            cl.display()

        break

    elif choice == "c":
        class Node:
            def __init__(self, next=None, data=None):
                self.next = next
                self.data = data


        def push(head_ref, data):
            ptr = Node()
            ptr.data = data
            ptr.next = head_ref

            if (head_ref != None):

                temp = head_ref
                while (temp.next != head_ref):
                    temp = temp.next
                temp.next = ptr

            else:
                ptr.next = ptr

            head_ref = ptr
            return head_ref


        def deleteNode(head, key):
            if (head == None):
                return

            if ((head).data == key and (head).next == head):
                head = None

            last = head
            d = None

            if ((head).data == key):

                while (last.next != head):
                    last = last.next

                last.next = (head).next
                head = last.next

            while (last.next != head and last.next.data != key):
                last = last.next

            if (last.next.data == key):
                d = last.next
                last.next = d.next

            else:
                print("No such key found")

            return head

        def printList(head):
            temp = head
            if (head != None):
                while (True):
                    print(temp.data, end=" ")
                    temp = temp.next
                    if (temp == head):
                        break
            print()

        head = None
        print("Deletion:")
        head = push(head, input("Enter items:"))
        head = push(head, input("Enter items:"))
        head = push(head, input("Enter items:"))

        print("List Before Deletion: ")
        printList(head)

        head = deleteNode(head, input("Enter the item to be deleted:"))

        print("List After Deletion: ")
        printList(head)

        break

    elif choice == "d":
        class Node:

            def __init__(self, data):
                self.data = data
                self.next = None

        class CircularLinkedList:

            def __init__(self):
                self.head = None

            def push(self, data):
                ptr = Node(data)
                temp = self.head

                ptr.next = self.head

                if self.head is not None:
                    while (temp.next != self.head):
                        temp = temp.next
                    temp.next = ptr

                else:
                    ptr.next = ptr

                self.head = ptr

            def printList(self):
                temp = self.head
                if self.head is not None:
                    while (True):
                        print(temp.data, end=" ")
                        temp = temp.next
                        if (temp == self.head):
                            break

        cllist = CircularLinkedList()
        print("Traversal:")
        cllist.push(input("Enter:"))
        cllist.push(input("Enter:"))
        cllist.push(input("Enter:"))
        cllist.push(input("Enter:"))

        print("Contents of circular Linked List")
        cllist.printList()

        break




print("a. Creation")
print("b. Insertion")
print("c. Deletion")
print("d. Traversal")
while(True):
    choice = input("Select a choice:")
    if choice == "a":
        class node(object):

            def __init__(self, data=None, next=None, prev=None):
                self.data = data
                self.next = next
                self.prev = prev


        class doubly_linked_list(object):
            def __init__(self):
                self.head = None
                self.tail = None
                self.count = 0

            def append_item(self, data):
                new_item = node(data, None, None)
                if self.head is None:
                    self.head = new_item
                    self.tail = self.head
                else:
                    new_item.prev = self.tail
                    self.tail.next = new_item
                    self.tail = new_item
                self.count += 1

            def iter(self):
                current = self.head
                while current:
                    item_val = current.data
                    current = current.next
                    yield item_val

            def forward(self):
                for node in self.iter():
                    print(node)


        items = doubly_linked_list()
        print("Creation:")
        items.append_item(input("Enter:"))
        items.append_item(input("Enter:"))
        items.append_item(input("Enter:"))
        items.append_item(input("Enter:"))

        print("List:")
        items.forward()

        break

    if choice == "b":
        class Node:
            def __init__(self, data):
                self.data = data
                self.next = None
                self.prev = None

        class doubly_linked_list:
            def __init__(self):
                self.head = None

            def push(self, NewVal):
                NewNode = Node(NewVal)
                NewNode.next = self.head
                if self.head is not None:
                    self.head.prev = NewNode
                self.head = NewNode

            def insert(self, prev_node, NewVal):
                if prev_node is None:
                    return
                NewNode = Node(NewVal)
                NewNode.next = prev_node.next
                prev_node.next = NewNode
                NewNode.prev = prev_node
                if NewNode.next is not None:
                    NewNode.next.prev = NewNode

            def listprint(self, node):
                while (node is not None):
                    print(node.data),
                    last = node
                    node = node.next

        dllist = doubly_linked_list()
        print("Insertion:")
        dllist.push(input("Enter:"))
        dllist.push(input("Enter:"))
        dllist.push(input("Enter:"))
        print("The list")
        dllist.listprint(dllist.head)
        dllist.insert(dllist.head.next, input("Enter the item to be inserted:"))
        print("The updated list after insertion")
        dllist.listprint(dllist.head)

        break

    if choice == "c":
        class Node(object):

            def __init__(self, value=None, next=None, prev=None):
                self.value = value
                self.next = next
                self.prev = prev


        class doubly_linked_list(object):
            def __init__(self):
                self.head = None
                self.tail = None
                self.count = 0

            def append_item(self, value):
                # Append an item
                new_item = Node(value, None, None)
                if self.head is None:
                    self.head = new_item
                    self.tail = self.head
                else:
                    new_item.prev = self.tail
                    self.tail.next = new_item
                    self.tail = new_item
                self.count += 1

            def iter(self):
                # Iterate the list
                current = self.head
                while current:
                    item_val = current.value
                    current = current.next
                    yield item_val

            def print_foward(self):
                for node in self.iter():
                    print(node)

            def search_item(self, val):
                for node in self.iter():
                    if val == node:
                        return True
                return False

            def delete(self, value):
                # Delete a specific item
                current = self.head
                node_deleted = False
                if current is None:
                    node_deleted = False

                elif current.value == value:
                    self.head = current.next
                    self.head.prev = None
                    node_deleted = True

                elif self.tail.value == value:
                    self.tail = self.tail.prev
                    self.tail.next = None
                    node_deleted = True

                else:
                    while current:
                        if current.value == value:
                            current.prev.next = current.next
                            current.next.prev = current.prev
                            node_deleted = True
                        current = current.next

                if node_deleted:
                    self.count -= 1


        items = doubly_linked_list()
        print("Deletion:")
        items.append_item(input("Enter:"))
        items.append_item(input("Enter:"))
        items.append_item(input("Enter:"))
        items.append_item(input("Enter:"))

        print("Original list:")
        items.print_foward()

        items.delete(input("Enter the item to be deleted:"))
        print("Updated list after deletion:")
        items.print_foward()

        break

    if choice == "d":
        class Node:

            def __init__(self, data):
                self.data = data
                self.next = None
                self.prev = None


        class DoubleLinkedList:

            def __init__(self):
                self.head = None

            def PrintList(self):
                temp = self.head
                if (temp != None):
                    print("The list contains:", end=" ")
                    while (temp != None):
                        print(temp.data, end=" ")
                        temp = temp.next
                    print()
                else:
                    print("The list is empty.")


        MyList = DoubleLinkedList()

        print("Traversal:")
        first = Node(input("Enter:"))
        MyList.head = first
        second = Node(input("Enter:"))
        second.prev = first
        first.next = second
        third = Node(input("Enter:"))
        third.prev = second
        second.next = third

        MyList.PrintList()

        break










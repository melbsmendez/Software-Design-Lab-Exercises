class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:

    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

    def EnQueue(self, item):
        temp = Node(item)

        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def DeQueue(self):

        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next

        if (self.front == None):
            self.rear = None

if __name__ == '__main__':
    q = Queue()
    q.EnQueue(input("Enter:"))
    q.EnQueue(input("Enter:"))
    q.EnQueue(input("Enter:"))
    q.EnQueue(input("Enter:"))
    q.EnQueue(input("Enter:"))
    q.DeQueue()
    q.DeQueue()
    q.DeQueue()

    print("Front:" + str(q.front.data))
    print("Rear:" + str(q.rear.data))


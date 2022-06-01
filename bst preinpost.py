class Node:
    def __init__(self, val):
        self.childleft = None
        self.childright = None
        self.nodedata = val

root = Node(1)
root.childleft = Node(2)
root.childright = Node(3)
root.childleft.childleft = Node(4)
root.childleft.childright = Node(5)

print("Pre-order:")
def Preord(root):
    if root:
        print(root.nodedata)
        Preord(root.childleft)
        Preord(root.childright)
Preord(root)

print("Post-order:")
def Postord(root):
    if root:
        Postord(root.childleft)
        Postord(root.childright)
        print(root.nodedata)
Postord(root)

print("In-order:")
def Inord(root):
    if root:
        Inord(root.childleft)
        print(root.nodedata)
        Inord(root.childright)
Inord(root)


class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def insert(root, key):
	if root is None:
		return Node(key)
	else:
		if root.val == key:
			return root
		elif root.val < key:
			root.right = insert(root.right, key)
		else:
			root.left = insert(root.left, key)
	return root

def inorder(root):
	if root:
		inorder(root.left)
		print(root.val)
		inorder(root.right)

def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

r = Node(input("Enter:"))
r = insert(r, input("Enter:"))
r = insert(r, input("Enter:"))
r = insert(r, input("Enter:"))
r = insert(r, input("Enter:"))
r = insert(r, input("Enter:"))
r = insert(r, input("Enter:"))

print("The tree:")
inorder(r)

print("Number of nodes in tree: {}".format(count_nodes(r)))


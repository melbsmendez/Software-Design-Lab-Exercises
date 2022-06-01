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

r = Node(input("Enter:"))
r = insert(r, input("Enter:"))
r = insert(r, input("Enter:"))
r = insert(r, input("Enter:"))
r = insert(r, input("Enter:"))
r = insert(r, input("Enter:"))
r = insert(r, input("Enter:"))

print("The tree:")
inorder(r)

import random

class BST:

	def __init__(self):
		self.head = Node(None)

	def insert(self, value):
		inserted = False
		curr = self.head
		print("inserting " + str(value))
		while (not inserted):
			
			# if head is empty
			if (curr.getValue() == None):
				self.head = Node(value)
				inserted = True
			elif (curr.getValue() > value):
				if (curr.getLeftChild() == None):
					curr.setLeftChild(value)
					inserted = True
				else:
					curr = curr.getLeftChild()
					pass
			elif (curr.getValue() < value):
				if (curr.getRightChild() == None):
					curr.setRightChild(value)
					inserted = True
				else:
					curr = curr.getRightChild()
			# if value is equal to current Node
			else:
				if (curr.setEmptyChild(value)):
					inserted = True
				else:
					curr = curr.getLeftChild()

	def search(self, value):
		found = False
		curr = self.head
		searching = True

		while (searching):
			if (curr.getValue() == value):
				print("BST contains " + str(value))
				found = True
				searching = False
			elif (curr.getValue() > value):
				if (not curr.hasLeftChild()):
					searching = False
				else:
					curr = curr.getLeftChild()
			elif (curr.getValue() < value):
				if (not curr.hasRightChild()):
					searching = False
				else:
					curr = curr.getRightChild()

		if (found):
			print("BST contains " + str(value))
		else:
		 	print("BST does not contain " + str(value))

		return found

	# def print(self):
	# 	self.output = {}
	# 	level = 0
	# 	self.__outputNode(self.head, self.output, level)
	# 	for i in range(0, len(self.output)):
	# 		print(self.output[i])

	def __outputNode(self, node, output, level):
		if (node.getLeftChild() != None):
			self.__outputNode(node.getLeftChild(), self.output, level + 1)
		if (node.getRightChild() != None):
			self.__outputNode(node.getRightChild(), self.output, level + 1)
		if (level not in self.output):
			self.output[level] = [node.getValue()]
		else:
			self.output[level].append(node.getValue())

	def __trans(self, node, type):
		if (type == "pre"):
			print(node.value, end=" ")
			if (node.hasLeftChild()):
				self.__trans(node.getLeftChild(), "pre")
			if (node.hasRightChild()):
				self.__trans(node.getRightChild(), "pre")
		elif (type == "in"):
			if (node.hasLeftChild()):
				self.__trans(node.getLeftChild(), "in")
			print(node.value, end=" ")
			if (node.hasRightChild()):
				self.__trans(node.getRightChild(), "in")
		elif (type == "post"):
			if (node.hasLeftChild()):
				self.__trans(node.getLeftChild(), "post")
			if (node.hasRightChild()):
				self.__trans(node.getRightChild(), "post")
			print(node.value, end=" ")
			

	def preTrans(self):
		self.__trans(self.head, "pre")
		print("")

	def inTrans(self):
		self.__trans(self.head, "in")
		print("")

	def postTrans(self):
		self.__trans(self.head, "post")
		print("")


class Node:

	def __init__(self, value):
		self.value = value
		self.leftChild = None
		self.rightChild = None

	def hasLeftChild(self):
		if (self.leftChild is not None):
			return True
		else:
			return False

	def hasRightChild(self):
		if (self.rightChild is not None):
			return True
		else:
			return False

	def setLeftChild(self, value):
		self.leftChild = Node(value)

	def setRightChild(self, value):
		self.rightChild = Node(value)

	def getLeftChild(self):
		return self.leftChild

	def getRightChild(self):
		return self.rightChild

	def getValue(self):
		return self.value

	def setEmptyChild(self, value):
		if (self.leftChild == None):
			self.leftChild = Node(value)
			return True
		elif (self.rightChild == None):
			self.rightChild = Node(value)
			return True
		else:
			return False


bst = BST()

for a in range(0, 5):
	bst.insert(random.randint(0, 10))

for a in range(0, 5):
	bst.search(random.randint(0, 10))

print("IN")
bst.inTrans()
print("PRE")
bst.preTrans()
print("POST")
bst.postTrans()
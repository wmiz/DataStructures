class Trie:

	def __init__(self):
		self.head = Node(None)

	def add(self, str):
		chars = list(str)

		curr = self.head

		for char in chars:
			if (curr.hasChild(char)):
				curr = curr.getChild(char)
			else:
				curr.setChild(Node(char))
				curr = curr.getChild(char)
		curr.setChild(Node("/"))

	def search(self, str):
		present = True
		chars = list(str)

		curr = self.head

		for char in chars:
			if (curr.hasChild(char)):
				curr = curr.getChild(char)
			else:
				present = False
				break
		if (curr.hasChild("/")):
			present = True
		else:
			present = False

		if (present):
			print(str + " found in trie")
		else:
			print(str + " not in trie")

	def listAll(self):
		if (not self.head.hasChildren()):
			print ("No words found in trie")
		else:
			self.process(self.head, "")

	def process(self, node, prefix):
		if (node.getValue() == "/"):
			print(prefix)
		else:
			if (node.getValue() != None):
				prefix = prefix + node.getValue()
			children = node.getChildren()
			for child in children:
				self.process(child, prefix)



class Node:

	def __init__(self, value):
		self.value = value
		self.children = []

	def setChild(self, node):
		self.children.append(node)

	def getChildren(self):
		return self.children

	def getValue(self):
		return self.value

	def hasChild(self, value):
		for child in self.children:
			if (child.getValue() == value):
				return True
		return False

	def getChild(self, value):
		for child in self.children:
			if (child.getValue() == value):
				return child
		return False

	def hasChildren(self):
		return len(self.children) >= 1

t = Trie()

t.add("dog")
t.add("frog")
t.add("dost")
t.add("dogger")
t.add("frogs")

t.search("dog")
t.search("frog")
t.search("dogger")
t.search("frogs")

t.search("do")
t.search("cat")

t.listAll()
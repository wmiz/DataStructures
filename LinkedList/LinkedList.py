class LinkedList:

	def __init__(self):
		self.head = LLNode(None)

	def append(self, data):
		if self.head.getNext() is None:
			self.head.setNext(LLNode(data))
		else:
			origNext = self.head.getNext()
			self.head.setNext(LLNode(data))
			self.head.getNext().setNext(origNext)

	def remove(self):
		self.head.setNext(self.head.getNext().getNext())

	def search(self, key):
		key = str(key)
		curr = self.head
		val = str(curr.getData())
		i = 0
		while (key != val):
			# print(key + " does not equal " + val)
			curr = curr.getNext()
			if (curr is None):
				return "Did not find key"
			val = str(curr.getData())
			i += 1
		return("Found key in index " + str(i - 1))

	def delete(self, key):
		key = str(key)
		curr = self.head
		prev = None
		val = str(curr.getData())
		while (key != val):
			prev = curr
			curr = curr.getNext()
			if (curr is None):
				return "Did not find key"
			val = str(curr.getData())
		prev.setNext(curr.getNext())

	def print(self):
		curr = self.head.getNext()
		while (curr != None):
			print(curr.data)
			curr = curr.getNext()


class LLNode:

	def __init__(self, data):
		self.data = data
		self.next = None

	def setData(self, data):
		self.data = data

	def setNext(self, node):
		self.next = node

	def getData(self):
		return self.data

	def getNext(self):
		return self.next


ll = LinkedList()
for x in range(6):
	# print("appending " + str(x))
	ll.append(x + 1)

ll.remove()
print(ll.search(4))
ll.delete(4)
ll.delete(3)
ll.print()
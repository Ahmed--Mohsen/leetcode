"""

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: 
get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

"""
class Node:	
	def __init__(self, key, val, prev=None, next=None):
		self.val = val
		self.key = key
		self.prev = prev
		self.next = next
		
class LinkedList:
	def __init__(self):
		self.size = 0
		self.head = Node(None, None)
		self.tail = Node(None, None)
		self.head.next = self.tail
		self.tail.prev = self.head
		
	def push(self, n):
		# link between n and head
		next = self.head.next
		self.head.next = n
		n.prev = self.head
		
		# link between n and next
		n.next = next
		next.prev = n
		
		#update size
		self.size = self.size + 1

		return n
	
	def pop(self):
		last = self.tail.prev
		prelast = last.prev
		prelast.next = self.tail
		self.tail.prev = prelast
		
		# update size
		self.size = self.size - 1
		
		return last
		
	def remove(self, node):
		prev = node.prev
		next = node.next
		prev.next = next
		next.prev = prev
		
		# update size
		self.size = self.size - 1
		
	def printList(self):
		pointer = self.head.next
		s = ""
		while(pointer != self.tail):
			s = s + str(pointer.val) + " , "
			pointer = pointer.next

		print s
		
		
class LRUCache:
	
	# @param capacity, an integer
	def __init__(self, capacity):
		self.memory = LinkedList()
		self.capacity = capacity
		self.keys = {}

	# @return an integer
	def get(self, key):
		if self.keys.has_key(key):
			# add key to the start of the list
			return self.refreshKey(key).val
		else:
			return -1

	# @param key, an integer
	# @param value, an integer
	# @return nothing
	def set(self, key, value):
		if self.keys.has_key(key):
			oldNode = self.refreshKey(key)
			oldNode.val = value
		else:
			if self.memory.size == self.capacity:
				invalidatedNode = self.memory.pop()
				invalidatedkey = invalidatedNode.key
				self.keys.pop(invalidatedkey, None) 
			
			# insert new key/value
			node = Node(key, value)
			self.memory.push(node)
			self.keys[key] = node

	
	def refreshKey(self, key):
		node = self.keys[key]
		self.memory.remove(node)
		self.memory.push(node)
		return node
		
		

l = LRUCache(1)
l.set(2,1)
print l.get(2)
l.set(3,2)
print l.get(2)
print l.get(3)



	
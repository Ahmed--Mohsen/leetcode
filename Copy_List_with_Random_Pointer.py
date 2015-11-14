"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

"""

# Definition for singly-linked list with a random pointer.
class RandomListNode:
	def __init__(self, x):
		self.label = x
		self.next = None
		self.random = None
	
	def __str__(self):
		return str(self.label)

class Solution:
	
	# @param head, a RandomListNode
	# @return a RandomListNode
	def copyRandomList(self, head):
		# baes case
		if head == None:
			return None

		# key = real node label , value = copy node
		map = {} 

		#copy head
		copyHead = self.getNodeCopy(map, head)
		
		pointer = head
		while pointer:

			# copy pointer node
			copyPointer = self.getNodeCopy(map, pointer)
			
			# copy its next pointer
			copyPointer.next = self.getNodeCopy(map, pointer.next)
			
			# copy its random pointer
			copyPointer.random = self.getNodeCopy(map, pointer.random)
			
			# move to next node
			pointer = pointer.next

		return copyHead
			

	"""
	get a copy node for the input node
	if the node copy already existed before its just returned
	"""
	def getNodeCopy(self, map,  node):
		# for non refrenced edges
		if node == None:
			return None
			
		# not copied before
		if not node in map:
			copy = RandomListNode(node.label)
			map[node] = copy
			
		return map[node]



head = RandomListNode(3)
head.next = RandomListNode(5)
s = Solution()
x = s.copyRandomList(head)
count = 0
while x and count < 10:	
	print x.label, 
	x = x.next
	count += 1
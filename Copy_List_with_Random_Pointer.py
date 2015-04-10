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
		visited = {} #original to copy mapping
		
		pointer = head
		pre_copy = RandomListNode(-1)
		copy_pointer = pre_copy
		while pointer:
			
			#handling next link
			if not pointer in visited:
				copy_node = RandomListNode(pointer.label)
				visited[pointer] = copy_node
			else:
				copy_node = visited[pointer]
			
			copy_pointer.next = copy_node
			copy_pointer = copy_pointer.next
			
			#handling random link
			if pointer.random:
				if not pointer.random in visited:
					copy_random = RandomListNode(pointer.random.label)
					visited[pointer.random] = copy_random
				else:
					copy_random = visited[pointer.random]
					
				copy_node.random = copy_random
				
			pointer = pointer.next
		
		return pre_copy.next
			

head = RandomListNode(3)
head.next = RandomListNode(5)
s = Solution()
x = s.copyRandomList(head)
count = 0
while x and count < 10:	
	print x.label, 
	x = x.next
	count += 1
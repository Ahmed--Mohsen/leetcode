"""

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.

"""

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param head, a ListNode
	# @param x, an integer
	# @return a ListNode
	def partition(self, head, x):
		current = head
		
		# points to elemets less than x
		less_head = ListNode(-1); less = less_head
		
		# points to elements more than or equal x
		more_head = ListNode(-1); more = more_head
		
		while current:
			if current.val < x:
				less.next = current
				less = less.next
			else: # current.val >= x
				more.next = current
				more = more.next
			current = current.next
		
		# merge less and more heads
		less.next = more_head.next
		more.next = None
		
		return less_head.next

	def printList(self, head, size=100):
		pointer = head
		s = ""
		counter = 0
		while pointer != None and counter < size:
			s = s + str(pointer.val) + " , "
			pointer = pointer.next
			counter = counter + 1
		print s



s = Solution()

vals = [1, 4, 3, 2, 5, 2]
prev_head = ListNode(-1)
prev = prev_head
for val in vals:
	current = ListNode(val)
	prev.next = current
	prev = current
	
s.printList(prev_head.next)
partitioned = s.partition(prev_head.next, 3)
s.printList(partitioned)


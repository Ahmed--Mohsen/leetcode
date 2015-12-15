# -*- coding: utf-8 -*-
"""

Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.

"""

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param head, a ListNode
	# @param m, an integer
	# @param n, an integer
	# @return a ListNode
	def reverseBetween(self, head, m, n):
		# use a pre head node to handle case when m = 1
		dummy = ListNode(0)
		dummy.next = head
		
		# points to the prev node to the m node
		start = dummy		
		for i in range(m-1):
			start = start.next
		
		# points to the next node to the n node
		end = dummy
		for i in range(n+1):
			end = end.next
		
		
		# keep track of the node to be attached to end
		prev_end = start.next
		
		# start reversing from start.next till end
		prev = start.next
		current = prev.next
		while current != end:
			
			# keep next pointer
			next = current.next
			
			# reverse links
			current.next = prev
			
			# increment pointers
			prev = current
			current = next
		
		# set links for start and end
		start.next = prev
		prev_end.next = end
		
		return dummy.next
		
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
head = ListNode(1)
pointer = head

for i in range(2,6,1):
	temp = ListNode(i)
	pointer.next = temp
	pointer = pointer.next

s.printList(head)
x = s.reverseBetween(head, 1, 5)
s.printList(x)

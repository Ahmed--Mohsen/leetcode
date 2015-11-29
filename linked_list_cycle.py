"""

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

"""

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param head, a ListNode
	# @return a boolean
	def hasCycle(self, head):
		# slow runner pointers
		slow = head
		fast = head
		
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
			
			if fast == slow:
				return True
		
		# no cycles detecetd
		return False

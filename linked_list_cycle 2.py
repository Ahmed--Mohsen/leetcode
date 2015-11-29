"""

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

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
	def detectCycle(self, head):
		slow = head
		fast = head
		
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
			
			if fast == slow:
				break
		
		# no cycles detecetd
		if fast == None or fast.next == None:
			return None
		
		# detect the cycle starting node
		slow = head
		while slow != fast:
			slow = slow.next
			fast = fast.next
		
		return slow

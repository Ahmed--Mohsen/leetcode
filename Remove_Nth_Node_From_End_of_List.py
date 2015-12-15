"""

Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	
	# @return a ListNode
	def removeNthFromEnd(self, head, n):
		slow = head
		fast = head
		
		# keep the distabce between slow and fast n steps
		for	i in range(n):
			fast = fast.next
		
		# list length is less than n ... remove head
		if fast == None: 
			return head.next
		
		# move till slow.next point to the nth node
		while fast.next:
			slow = slow.next
			fast = fast.next
		
		# remove the node
		slow.next = slow.next.next
		
		return head
		
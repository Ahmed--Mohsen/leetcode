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
		
		for	i in range(n):
			fast = fast.next
		
		if fast == None: #list length is less than n
			return slow.next
		
		while fast.next != None:
			slow = slow.next
			fast = fast.next
		
		#remove the node
		slow.next = slow.next.next
		return head
		
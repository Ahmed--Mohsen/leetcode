"""

Sort a linked list in O(n log n) time using constant space complexity.

"""

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	
	"""
	:type head: ListNode
	:rtype: ListNode
	"""
	def sortList(self, head):
		# base case
		if	head == None or head.next == None:
			return head
		
		# split the list into 2 halves
		left, right = self.split(head)
		
		# sort each half
		left = self.sortList(left)
		right = self.sortList(right)
		
		# merge sorted halves into on list
		return self.merge(left, right)
		
	
	"""
	:desc cut a linked list into equal sized halves
	:type head: ListNode
	:rtype: (ListNode, ListNode)
	"""
	def split(self, head):
		slow = head
		fast = head
		while fast.next and fast.next.next:
			slow = slow.next
			fast = fast.next.next
		
		# terminate first half (head)
		half_head = slow.next
		slow.next = None

		return (head, half_head)
	
	
	"""
	:desc merge 2 sorted lists into one
	:type left: ListNode
	:type right: ListNode
	:rtype: ListNode
	"""
	def merge(self, left, right):		
		
		preHead = ListNode(-1)
		pointer = preHead
		
		while left and right:
			# merge left first
			if left.val < right.val:
				pointer.next = left
				left = left.next
				
			# merge right first
			else:
				pointer.next = right
				right = right.next
			
			# move forward
			pointer = pointer.next
				
		# merge remaining parts
		if left != None:
			pointer.next = left
		
		if right != None:
			pointer.next = right
			
		return preHead.next
	
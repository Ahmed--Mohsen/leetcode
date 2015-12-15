# -*- coding: utf-8 -*-
"""

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.

"""

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	
	"""
	:type head: ListNode
	:rtype: void Do not return anything, modify head in-place instead.
	"""
	def reorderList(self, head):
		# base case
		if head == None or head.next == None:
			return
			
		# split the list into 2 halves
		first, second = self.split(head)
		
		# reverse second half
		second = self.reverse(second)
		
		# merge in the required pattern
		self.merge(first, second)
		
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
	:desc reverse a linked list
	:type head: ListNode
	:rtype: ListNode
	"""
	def reverse(self, head):
		prev = None
		current = head
		while current:
			# reverse links
			next = current.next
			current.next = prev 
	
			# update pointers
			prev = current
			current = next
		
		return prev
	
	
	"""
	:desc merge 2 linked lists according to the problem
	:type first: ListNode
	:type second: ListNode
	:rtype: void
	"""
	def merge(self, first, second):
		p1 = first 
		p2 = second
		while p1 and p2:
			
			# keep track of next pointers
			p1Next = p1.next
			p2Next = p2.next
			
			# merge in zigzag pattern
			p1.next = p2
			p2.next = p1Next
			
			# move to next nodes
			p1 = p1Next
			p2 = p2Next
		
		
		
	def printList(self, head):
		pointer = head
		s = ""
		while pointer != None:
			s = s + str(pointer.val) + " , "
			pointer = pointer.next
		print s


s = Solution()
head = ListNode(1)
pointer = head
for i in range(2,3,1):
	temp = ListNode(i)
	pointer.next = temp
	pointer = pointer.next
	
s.printList(s.reorderList(head))
#s.printList(s.reverse(head))

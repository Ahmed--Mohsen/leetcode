# -*- coding: utf-8 -*-
"""

Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

"""

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None
	
	def __str__(self):
		return str(self.val)

class Solution:
	
	# @param two ListNodes
	# @return the intersected ListNode
	def getIntersectionNode(self, headA, headB):
		
		# get the size for both lists
		size_a = self.size(headA)
		size_b = self.size(headB)
		p_a = headA; p_b = headB
		
		# make both pointer to be equally distant from there tails
		p_a = self.advance_to(p_a, size_a - size_b)
		p_b = self.advance_to(p_b, size_b - size_a)
		
		# move the 2 pointers by the same speed till they collide
		while p_a != p_b:
			
			# update both pointers
			p_a = p_a.next
			p_b = p_b.next
		
		# first intersection p_a = p_b here
		return p_a
	
	def size(self, head):
		pointer = head
		count = 0
		while pointer:
			count += 1
			pointer = pointer.next
		return count
	
	def advance_to(self, pointer, steps):
		while steps > 0 :
			pointer = pointer.next
			steps -= 1
		return pointer
			
			
s = Solution()
l = ListNode(3)
l2 = ListNode(2)
l2.next = ListNode(3)
l.next = l2.next
x = s.getIntersectionNode(l,l2)
print x

"""

Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

"""

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	
	# @param two ListNodes
	# @return a ListNode
	def mergeTwoLists(self, l1, l2):
		
		# base cases
		if l1 == None: return l2
		if l2 == None: return l1
			
		# pointers to l1 and l2
		p1 = l1
		p2 = l2
		
		# dummy node pointing to merged list
		dummy = ListNode(-1)
		p_merged = dummy
		
		# while both lists has remaining nodes
		while p1 and p2:
			
			# merge p1 first
			if p1.val <= p2.val:
				p_merged.next = p1
				p1 = p1.next
				
			# meege p2 first
			else:
				p_merged.next = p2
				p2 = p2.next
			
			# update the merged pointer
			p_merged = p_merged.next
		
		# concateante the remaining list that haven't merged
		# when the 2 list are not of the same length
		if p1 == None:
			p_merged.next = p2
		
		if p2 == None:
			p_merged.next = p1
		
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

p1 = ListNode(1)
p2 = ListNode(2)
s.printList(s.mergeTwoLists(p1, p2))
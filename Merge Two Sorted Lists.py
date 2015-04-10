# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param two ListNodes
	# @return a ListNode
	def mergeTwoLists(self, l1, l2):
		if l1 == None and l2 == None:
			return None
		
		if l1 == None:
			return l2
		
		if l2 == None:
			return l1
			
		
		p1 = l1
		p2 = l2
		pre_sorted = ListNode(-1)
		p_sorted = pre_sorted
		
		while p1 != None and p2 != None:
			if p1.val <= p2.val:
				p_sorted.next = p1
				p1 = p1.next
			else:
				p_sorted.next = p2
				p2 = p2.next
			p_sorted = p_sorted.next
		
		#concateante the remaining list
		if p1 == None:
			p_sorted.next = p2
		
		if p2 == None:
			p_sorted.next = p1
		
		return pre_sorted.next
		
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
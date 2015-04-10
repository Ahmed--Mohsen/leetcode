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
		size_a = self.size(headA)
		size_b = self.size(headB)
		p_a = headA; p_b = headB
		
		#make both pointer are equally distant from there tails
		if size_a > size_b:
			p_a = self.advance_to(p_a, size_a - size_b)
		elif size_b > size_a:
			p_b = self.advance_to(p_b, size_b - size_a)

		latest_intersection = None
		while p_a and p_b and latest_intersection == None:
			 #intersection occured
			if p_a.val == p_b.val:
				latest_intersection = p_a
			
			#update both pointers
			p_a = p_a.next
			p_b = p_b.next
		
		return latest_intersection		

	
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
x = s.getIntersectionNode(l,l2)
print x.val

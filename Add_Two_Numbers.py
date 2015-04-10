# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @return a ListNode
	def addTwoNumbers(self, l1, l2):
		if l1 == None and l2 == None:
			return None
		if l1 == None:
			return l2
		if l2 == None:
			return l1
		
		n1 = l1
		n2 = l2
		carry = 0
		result = ListNode(-1)
		pointer = result
		
		while n1 != None or n2 != None or carry != 0:	
			a = n1.val if n1 != None else 0
			b = n2.val if n2 != None else 0
			total = a + b + carry
			remainder = total % 10
			carry = total / 10
			sum_node = ListNode(remainder)
			pointer.next = sum_node
			
			pointer = pointer.next
			if n1 != None:
				n1 = n1.next
			if n2 != None:
				n2 = n2.next
			
		return result.next
		
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
l1 = ListNode(9)
pointer = l1
for i in range(2,3,1):
	temp = ListNode(i)
	pointer.next = temp
	pointer = pointer.next

l2 = ListNode(1)
pointer = l2
for i in range(2,3,1):
	temp = ListNode(9)
	pointer.next = temp
	pointer = pointer.next
	
x = s.addTwoNumbers(l1, l2)
s.printList(l1)
s.printList(l2)
s.printList(x)
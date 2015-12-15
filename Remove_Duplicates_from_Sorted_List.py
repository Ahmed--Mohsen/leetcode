"""

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

"""

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	
	# @param head, a ListNode
	# @return a ListNode
	def deleteDuplicates(self, head):
		if head == None:
			return head
	
		current = head
		while current.next:
			next = current.next
			if current.val == next.val:
				current.next = next.next
			else:
				current = current.next
		return head
		

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
head = ListNode(1)
pointer = head


for i in range(1,3,1):
	temp = ListNode(1)
	pointer.next = temp
	pointer = pointer.next

for i in range(1,4,1):
	temp = ListNode(2)
	pointer.next = temp
	pointer = pointer.next

for i in range(1,3,1):
	temp = ListNode(3)
	pointer.next = temp
	pointer = pointer.next

s.printList(head)
x = s.deleteDuplicates(head)
s.printList(x)
					

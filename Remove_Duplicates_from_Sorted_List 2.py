"""

Given a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

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
		# base case
		if head == None: return head
		
		# its next link will hold the answer
		dummy = ListNode(-1)
		dummy.next = head
		
		prev = dummy
		current = head
		
		while current:
			
			# skip nodes having same value
			while(current.next and current.val == current.next.val):
				current = current.next
				
			# no duplication
			if prev.next == current: 
				prev = current
				
			# duplication exist
			else: 
				prev.next = current.next
			
			# move to next node
			current = current.next
			
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
head = ListNode(5)
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
	
for i in range(1,2,1):
	temp = ListNode(6)
	pointer.next = temp
	pointer = pointer.next

s.printList(head)
x = s.deleteDuplicates(head)
s.printList(x)
					

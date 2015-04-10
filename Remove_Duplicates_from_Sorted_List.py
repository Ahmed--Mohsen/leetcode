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
		while current.next != None:
			next = current.next
			if current.val == next.val:
				current.next = next.next
			else:
				current = current.next
		return head
		
		
	# @param head, a ListNode
	# @return a ListNode
	def deleteDuplicatesOld(self, head):
		if head == None:
			return head
	
		start = head
		while start != None:
			end = start.next
			while end != None and start.val == end.val:
				end = end.next
			start.next = end
			start = start.next

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
					

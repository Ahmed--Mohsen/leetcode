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
			
		dummy = ListNode(-1)
		dummy.next = head
		
		prev = dummy
		current = head
		while current != None:
			while(current.next != None and current.val == current.next.val):
				current = current.next

			if prev.next == current: #no duplication
				prev = current
			else: #duplication exist
				prev.next = current.next
			current = current.next
		return dummy.next
		
		
	# @param head, a ListNode
	# @return a ListNode
	def deleteDuplicatesOld(self, head):
		if head == None:
			return head
		dummy = ListNode(-1)
		dummy.next = head
		
		prev = dummy
		start = head
		while start != None:
			end = start.next
			while end != None and start.val == end.val:
				end = end.next
			
			self.printList(dummy.next)
			if prev.next == end:
				prev = prev.next
			else:
				prev.next = end.next
			start = end.next

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
					

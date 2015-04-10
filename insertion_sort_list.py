# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param head, a ListNode
	# @return a ListNode
	def insertionSortList(self, head):
		# list is empty or contains one element
		if	head == None or head.next == None:
			return head
		
		sorted_head = ListNode(-1)
		pointer = head 			#points to unsorted portion of the list
		inner = sorted_head #points to sorted portion of the list
		
		while pointer != None:
			#reset inner pointer only when its value is larger than pointer
			if inner.val > pointer.val: 
				inner = sorted_head
			
			# save reference for next element to be sorted
			next_pointer = pointer.next
			
			# move till find the place to insert pointer into sorted list
			while inner.next and inner.next.val < pointer.val:
				inner = inner.next
			
			# insert pointer between inner and inner.next
			next = inner.next
			inner.next = pointer
			pointer.next = next
			
			# move to next unsorted element
			pointer = next_pointer
					
		return sorted_head.next
		
		
		
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

for i in range(4,1,-1):
	temp = ListNode(i)
	pointer.next = temp
	pointer = pointer.next
x = s.insertionSortList(head)
s.printList(x)

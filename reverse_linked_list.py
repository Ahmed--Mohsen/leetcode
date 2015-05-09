# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None
		
class Solution:
	# @param {ListNode} head
	# @return {ListNode}
	# iterative solution
	def reverseList(self, head):
		# base case
		if head == None or head.next == None:
			return head
		
		prev = None
		current = head
		next = None
		
		while current:
			# save next current pointer
			next = current.next
			
			# reverse links
			current.next = prev
			
			# advance pointers
			prev = current
			current = next
		
		return prev
		

	# @param {ListNode} head
	# @return {ListNode}
	# recursive solution
	def reverseListRecursive(self, head):
		# base case
		if head == None or head.next == None:
			return head
		
		# rest of the list to be reversed
		next = head.next
		
		# prevent cycles
		head.next = None
		
		# reverse the rest elements
		reverse = self.reverseList(next)
		
		# connect the reversed part with the head
		next.next = head
		
		return reverse
		
						
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

for i in range(2,5,1):
	temp = ListNode(i)
	pointer.next = temp
	pointer = pointer.next

s.printList(head)
x = s.reverseList(head)
s.printList(x)

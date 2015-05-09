# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param {ListNode} head
	# @param {integer} val
	# @return {ListNode}
	def removeElements(self, head, val):
		# base case
		if head == None:
			return head
	
		pre_head = ListNode(-1)
		pre_head.next = head
		prev = pre_head
	
		pointer = head
		while pointer:
			if pointer.val == val: # element found
				prev.next = pointer.next
			else: # proceed to next element
				prev = prev.next
				
			pointer = pointer.next
	
		return pre_head.next


	def printList(self, head, size=10):
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
	temp = ListNode(i-1)
	pointer.next = temp
	pointer = pointer.next

s.printList(head)
x = s.removeElements(head,1)
s.printList(x)
				
				
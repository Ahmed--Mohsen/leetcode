"""

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

"""

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None
		
class Solution:
	# @param a ListNode
	# @return a ListNode
	def swapPairs(self, head):
		
		# base case ... single nodes
		if head == None or head.next == None:
			return head
			
		prev = ListNode(-1)
		prev.next = head 
		pointer = prev
		
		while pointer.next and pointer.next.next:
			first = pointer.next
			second = first.next
			
			# reverse
			first.next = second.next
			second.next = first
			pointer.next = second
			
			# move forward
			pointer = first
		
		return prev.next


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
head1 = ListNode(1)
pointer = head1
for i in range(2,3,1):
	temp = ListNode(i)
	pointer.next = temp
	pointer = pointer.next

s.printList(head1)

x = s.swapPairs(head1)
s.printList(x)
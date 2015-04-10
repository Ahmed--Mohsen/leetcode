# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param head, a ListNode
	# @param m, an integer
	# @param n, an integer
	# @return a ListNode
	def reverseBetween(self, head, m, n):
		dummy = ListNode(0)
		dummy.next = head
		start = dummy
		
		
		#make start point to m-1 node and keep end diff
		diff = m-1
		while diff != 0:
			start = start.next
			diff -= 1
			n -= 1

		#start reversing
		pointer = start.next
		next = pointer.next
		
		while n-1 != 0:
			next_next = next.next
			next.next = pointer
			pointer = next
			next = next_next
			n -= 1
			
		#final reversal
		start.next.next = next
		start.next = pointer
		
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
head = ListNode(1)
pointer = head

for i in range(2,8,1):
	temp = ListNode(i)
	pointer.next = temp
	pointer = pointer.next

s.printList(head)
x = s.reverseBetween(head, 2, 4)
s.printList(x)

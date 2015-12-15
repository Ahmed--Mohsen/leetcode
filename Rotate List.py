"""

Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

"""

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param head, a ListNode
	# @param k, an integer
	# @return a ListNode
	def rotateRight(self, head, k):
		
		# base case
		if head == None:
			return head
		
		# keep track of two pointers with k nodes in between
		slow = head 
		fast = head
		
		# for large k values
		size = self.size(head)
		k = k % size 
		
		count = 0
		while fast and count < k:
			fast = fast.next
			count += 1
		
		# k is bigger than size
		if fast == None:
			return head
		
		# move pointers till end of list
		while fast.next != None:
			slow = slow.next
			fast = fast.next
		
		# start rotation
		fast.next = head # circle the list
		new_head = slow.next
		slow.next = None # break the cycle
		
		return new_head
	
	
	# calc size of a linked list	
	def size(self, head):
		size = 0
		pointer = head
		
		while pointer != None:
			size += 1
			pointer = pointer.next
		return size
		
		

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

for i in range(2,3,1):
	temp = ListNode(i)
	pointer.next = temp
	pointer = pointer.next
	
s.printList(head)
x = s.rotateRight(head,2)
s.printList(x)
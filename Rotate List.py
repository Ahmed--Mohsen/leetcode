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
		if head == None:
			return head
		
		slow = head 
		fast = head
		size = self.size(head)
		k = k % size #for large k values
		
		count = 0
		while fast != None and count < k:
			fast = fast.next
			count += 1
		
		if fast == None:
			return head

		while fast.next != None:
			slow = slow.next
			fast = fast.next
		
		#start rotation
		fast.next = head
		new_head = slow.next
		slow.next = None
		
		return new_head
		
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
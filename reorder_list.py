# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param head, a ListNode
	# @return nothing
	def reorderList(self, head):
		if head == None or head.next == None:
			return head
			
		#split the list into 2 halves
		slow = head
		fast = head
		while(slow != None and fast != None  and fast.next != None):
			slow = slow.next
			fast = fast.next.next
		
		first = head
		second = slow.next
		second = self.reverse(second)
		slow.next = None
		return self.merge(first,second)
	
	def reverse(self, head):
		prev = None
		current = head
		next = None
		
		while(current != None):
			next = current.next
			current.next = prev
			prev = current
			current = next
		head = prev
		
		return head
	
	def merge(self, first, second):
		p1 = first 
		p2 = second
		while(p1 != None and p2 != None):
			p1Next = p1.next
			p2Next = p2.next
			p1.next = p2
			p2.next = p1Next
			p1 = p1Next
			p2 = p2Next
		return first
		
		
	def printList(self, head):
		pointer = head
		s = ""
		while pointer != None:
			s = s + str(pointer.val) + " , "
			pointer = pointer.next
		print s


s = Solution()
head = ListNode(1)
pointer = head
for i in range(2,3,1):
	temp = ListNode(i)
	pointer.next = temp
	pointer = pointer.next
	
s.printList(s.reorderList(head))
#s.printList(s.reverse(head))

"""

Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?

"""

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	
	"""
	:type head: ListNode
	:rtype: bool
	"""
	def isPalindrome(self, head):
		# base case ... nothing or single node 
		if head == None or head.next == None:
			return True
		
		# split the list into halves
		head1, head2 = self.split(head)

		# reverse next half
		head2 = self.reverse(head2)

		# now to be palndirom head1 and head2
		# have to be the same
		while head1 and head2:
			if head1.val != head2.val:
				return False
			
			head1 = head1.next
			head2 = head2.next
		
		# true in both even and odd cases
		return True
		
	
	"""
	:desc cut a linked list into equal sized halves
	:type head: ListNode
	:rtype: (ListNode, ListNode)
	"""
	def split(self, head):
		slow = head
		fast = head
		while fast.next and fast.next.next:
			slow = slow.next
			fast = fast.next.next
		
		# terminate first half (head)
		half_head = slow.next
		slow.next = None

		return (head, half_head)

	"""
	:desc reverse a linked list
	:type head: ListNode
	:rtype: ListNode
	"""
	def reverse(self, head):
		prev = None
		current = head
		while current:
			# reverse links
			next = current.next
			current.next = prev 
	
			# update pointers
			prev = current
			current = next
		
		return prev
		

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
for i in range(2,4):
	temp = ListNode(i)
	pointer.next = temp
	pointer = pointer.next

for i in range(3,0,-1):
	temp = ListNode(i)
	pointer.next = temp
	pointer = pointer.next

s.printList(head)
print s.isPalindrome(head)
		


			
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
		slow = head
		fast = head
		while fast.next and fast.next.next:
			slow = slow.next
			fast = fast.next.next
		
		# terminate first half (head)
		head_rev = slow.next
		slow.next = None

		# reverse next half
		prev = None
		current = head_rev
		while current:
			# reverse links
			next = current.next
			current.next = prev 
			
			# update pointers
			prev = current
			current = next
		head_rev = prev
		
		# now to be palndirom head and head_rev
		# have to be the same
		while head and head_rev:
			if head.val != head_rev.val:
				return False
			
			head = head.next
			head_rev = head_rev.next
		
		# true in both even and odd cases
		return True
		

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
		


			
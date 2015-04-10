# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	# @param head, a ListNode
	# @return a boolean
	def detectCycle(self, head):
		prev = None
		pointer = head
		while(pointer != None):
			isVisited = getattr(pointer, 'visited', False)
			if isVisited:
				return prev
			pointer.visited = True
			prev = pointer
			pointer = pointer.next
		return None

s = Solution()
head = ListNode(1)
pointer = head
for i in range(2,5,1):
	temp = ListNode(i)
	pointer.next = temp
	pointer = pointer.next
pointer.next = head
print s.detectCycle(head).val
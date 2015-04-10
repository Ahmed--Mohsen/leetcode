# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	# @param head, a ListNode
	# @return a boolean
	def hasCycle(self, head):
		pointer = head
		while(pointer != None):
			isVisited = getattr(pointer, 'visited', False)
			if isVisited:
				return True
			pointer.visited = True
			pointer = pointer.next
		return False

s = Solution()
head = ListNode(1)
pointer = head
for i in range(2,3,1):
	temp = ListNode(i)
	pointer.next = temp
	pointer = pointer.next
pointer.next = head
print s.hasCycle(head)
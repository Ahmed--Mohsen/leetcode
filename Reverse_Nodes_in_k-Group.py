"""

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5


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
	def reverseKGroup(self, head, k):
		if head == None or k == 1:
			return head
		slow = head
		dummy = ListNode(-1)
		prev = dummy

		while slow:
			fast = slow
			
			# advance fast to be ahead of slow by k steps
			count = 0
			while fast and count < k:
				fast = fast.next
				count += 1
				 
			# list size is less than k
			if count < k: 
				prev.next = slow
				break

			# start reversing
			pointer = slow
			next = pointer.next
			for i in range(k-1):
				temp_next = next.next
				next.next = pointer
				pointer = next
				next = temp_next
			slow.next = fast
			
			# update for next step
			prev.next = pointer
			prev = slow
			slow = fast
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
x = s.reverseKGroup(head,3)
s.printList(x)
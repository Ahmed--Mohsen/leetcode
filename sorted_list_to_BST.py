"""

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

"""

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	
	# @param head, a list node
	# @return a tree node
	def sortedListToBST(self, head):
		# base case
		if head == None:
			return None
		
		return self.sortedListToBSTHelper(head, None)
	
	def sortedListToBSTHelper(self, head, tail):
		# base case
		if head == tail:
			return None
		
		# get the middle element (root)
		mid = head
		runner = head
		while runner.next != tail and runner.next.next != tail:
			mid = mid.next
			runner = runner.next.next
			
		#	set root node
		root = TreeNode(mid.val)
		
		# set its children
		root.left = self.sortedListToBSTHelper(head, mid)
		root.right = self.sortedListToBSTHelper(mid.next, tail)

		return root
	
s = Solution()
t1 = ListNode(3)
t2 = ListNode(5)
t3 = ListNode(8)
t1.next = t2
t2.next = t3
s.sortedListToBST(t1).val
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
		if head == None:
			return None
		
		pointer = head
		size = 0
		while(pointer != None):
			size += 1
			pointer = pointer.next
		self.list = head
		return self.sortedListToBSTHelper(0, size - 1)
	
	def sortedListToBSTHelper(self, low, high):
		#base case
		if low > high:
			return None
		
		mid = (low+high)/2
		left_child = self.sortedListToBSTHelper(low, mid - 1)
		root = TreeNode(self.list.val)
		print self.list.val
		root.left = left_child
		self.list = self.list.next
		root.right = self.sortedListToBSTHelper(mid + 1, high)
		return root
	
s = Solution()
t1 = ListNode(3)
t2 = ListNode(5)
t3 = ListNode(8)
t1.next = t2
t2.next = t3
s.sortedListToBST(t1).val
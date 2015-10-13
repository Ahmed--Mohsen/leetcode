# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	
	"""
	:type node: ListNode
	:rtype: void Do not return anything, modify node in-place instead.
	"""
	def deleteNode(self, node):
		# to delete a node I need its prev node so we will
		# swap the nodes values with its next one and delete
		# its next node
		node.val = node.next.val
		node.next = node.next.next
		

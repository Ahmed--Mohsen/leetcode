"""

Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
		

"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
	
	# @param root, a tree node
	# @return nothing
	def connect(self, root):
		
		# base case
		if root == None:
			return
		
		# traverse the tree while there is a left child
		pointer = root
		while pointer.left:
			current = pointer
			
			# connect all siblings on same level
			while current:
				
				# inner link
				current.left.next = current.right
				
				# outer link
				if current.next:
					current.right.next = current.next.left
					
				# move to next sibling on same level
				current = current.next
			
			# move to next child 
			pointer = pointer.left
	
	
	
	########################### Another Solution (Recursive) ###########################
	# @param root, a tree node
	# @return nothing
	def connect(self, root):
		# base case
		if root == None: return
			
		self.connect(root.left)
		self.connect(root.right)
		
		left = root.left
		right = root.right
		
		while left:
			left.next = right
			left = left.right
			right = right.left
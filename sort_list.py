# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param head, a ListNode
	# @return a ListNode
	def sortList(self, head):
		if	head == None or head.next == None:
			return head
		
		# get list size
		size = 0
		pointer = head
		while pointer != None:
			size = size + 1
			pointer = pointer.next
	
		return self.mergeSort(head, size)
	
	def mergeSort(self, head, size):
		#base case
		if size == 1:
			temp = head
			temp.next = None
			return temp
			
		#split the list into left and right sublists
		leftHead = head
		rightHead = head
		mid = (size)/2
		for	i in range(0, mid):
			rightHead = rightHead.next
					
		left = self.mergeSort(leftHead, mid)
		right = self.mergeSort(rightHead, size - mid)
		
		return self.merge(left, mid, right, size - mid)
	
	def merge(self, left, leftSize, right, rightSize):		
		if left == None:
			return right
		if right == None:
			return left
			
		preHead = ListNode(-1)
		pointer = preHead
		i = 0
		j = 0
		while(i < leftSize and j < rightSize):
			if left.val < right.val:
				pointer.next = left
				left = left.next
				i = i + 1
			else:
				pointer.next = right
				right = right.next
				j = j + 1
			pointer = pointer.next
				
		#merge remaining parts
		if left != None:
			pointer.next = left
		
		if right != None:
			pointer.next = right
			
		return preHead.next
	
	def printList(self, head, size=100):
		pointer = head
		s = ""
		counter = 0
		while pointer != None and counter < size:
			s = s + str(pointer.val) + " , "
			pointer = pointer.next
			counter = counter + 1
		print s
"""
s = Solution()
head = ListNode(1)
pointer = head
for i in range(20,11,-1):
	temp = ListNode(i)
	pointer.next = temp
	pointer = pointer.next
x = s.sortList(head)
s.printList(x)
"""
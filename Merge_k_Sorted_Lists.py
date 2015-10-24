import heapq

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None
		
class Solution:
	# @param a list of ListNode
	# @return a ListNode
	def mergeKLists(self, lists):
		#base cases
		if len(lists) == 0:
			return None
		if len(lists) == 1:
			return lists[0]
		
		pre_sort_head = ListNode(-1) # dummy
		pointer = pre_sort_head
		heap = []
		
		for list_node in lists:
			if list_node:
				heapq.heappush(heap, (list_node.val, list_node))
		
		while len(heap) > 0:
			
			# get min node and add it to the sorted list
			min_node = heapq.heappop(heap)[1]
			pointer.next = min_node
			pointer = pointer.next
			
			if min_node.next:
				heapq.heappush(heap, (min_node.next.val, min_node.next))
		
		return pre_sort_head.next	
	
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
head1 = ListNode(1)
pointer = head1
for i in range(4,10,3):
	temp = ListNode(i)
	pointer.next = temp
	pointer = pointer.next
	
head2 = ListNode(2)
pointer = head2
for i in range(5,10,3):
	temp = ListNode(i)
	pointer.next = temp
	pointer = pointer.next
	
head3 = ListNode(3)
pointer = head3
for i in range(6,10,3):
	temp = ListNode(i)
	pointer.next = temp
	pointer = pointer.next
	
	
s.printList(head1)
s.printList(head2)
s.printList(head3)
print "\n"
x = s.mergeKLists([head1, head2, head3])
#s.sortList(head)
s.printList(x)



	
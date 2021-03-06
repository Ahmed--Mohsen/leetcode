"""

Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.

"""

class Solution:
	
	# @param num, a list of integer
	# @return an integer
	def findMin(self, num):
		if len(num) == 1:
			return num[0]
			
		start = 0
		end = len(num) - 1
		
		while start < end:
			
			mid = ( start + end ) / 2
			
			# left is sorted
			if num[mid] > num[end]: 
				start = mid + 1
			
			# right is sorted
			elif num[mid] < num[end]: 
				end = mid
			
			# num[mid] == num[end]
			else: 
				end -= 1
				
		return num[start]
		

s = Solution()
print s.findMin([1, 1])
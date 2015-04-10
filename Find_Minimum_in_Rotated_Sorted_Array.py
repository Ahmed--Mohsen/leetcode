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
			
			if num[start] < num[end]: #already sorted
				return num[start]
			
			if num[start] <= num[mid]: #left half is sorted
				start = mid + 1
			else: #right half is sorted
				end = mid
				
		return num[start]
		
			
		
########################## Another Solution ##########################

class Solution:
	# @param num, a list of integer
	# @return an integer
	def findMin(self, num):
		if len(num) == 1:
			return num[0]
			
		start = 0
		end = len(num) - 1
		
		while start <= end:
			
			mid = ( start + end ) / 2
			
			if num[start] < num[end]: #already sorted
				return num[start]
			
			if num[mid] > num[mid+1]: #start of rotation
				return num[mid + 1]
			if num[mid-1] > num[mid]:
			    return num[mid]
			
			if num[start] < num[mid]: #left half is sorted
				start = mid + 1
			else: #right half is sorted
				end = mid - 1
		

s = Solution()
print s.findMin([1, 2])
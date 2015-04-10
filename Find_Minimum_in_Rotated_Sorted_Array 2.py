class Solution:
	# @param num, a list of integer
	# @return an integer
	def findMin(self, num):
		if len(num) == 1:
			return num[0]
			
		start = 0
		end = len(num) - 1
		
		while start < end and num[start] >= num[end]:
			
			mid = ( start + end ) / 2
			
			if num[mid] > num[end]: #right is sorted
				start = mid + 1
			elif num[mid] < num[start]: #left is sorted
				end = mid
			else: #num[start] = num[mid] = num[end]
				start += 1
		return num[start]
		

s = Solution()
print s.findMin([1, 1])
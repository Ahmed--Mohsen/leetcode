class Solution:
	# @return a list of lists of length 3, [[val1,val2,val3]]
	def threeSum(self, num):
		#base case
		if len(num) < 3:
			return []
		
		num.sort()
		result = []
		
		for i in range(len(num) - 2):
			if i == 0 or num[i] > num[i-1]: #check duplicates
				negate = -1 * num[i]				
				start = i + 1
				end = len(num) - 1
				while start < end:
					if num[start] + num[end] == negate: #found it
						result.append([num[i], num[start], num[end]])
						start += 1
						end -= 1
					
						#check duplicates
						while start < end and num[start] == num[start - 1]:
							start += 1
						
						while start < end and num[end] == num[end + 1]:
							end -= 1
					elif num[start] + num[end] > negate: #search for smaller
						end -= 1
					else: #search for bigger
						start += 1
		return result
	

s = Solution()				
print s.threeSum([-2,0,1,1,2])
		
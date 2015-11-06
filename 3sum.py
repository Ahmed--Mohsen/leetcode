"""

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
The solution set must not contain duplicate triplets.

"""

class Solution:
	# @return a list of lists of length 3, [[val1,val2,val3]]
	def threeSum(self, num):
		#base case
		if len(num) < 3:
			return []
		
		num.sort()
		result = []
		
		for i in range(len(num) - 2):
			
			# check duplicates
			if i == 0 or num[i] > num[i-1]: 
				
				negate = -1 * num[i]				
				start = i + 1
				end = len(num) - 1
				
				# find the numbers that sums up with negate to 0
				while start < end:
					
					# found it
					if num[start] + num[end] == negate: 
						result.append([num[i], num[start], num[end]])
						start += 1
						end -= 1
					
						# check duplicates
						while start < end and num[start] == num[start - 1]:
							start += 1
						while start < end and num[end] == num[end + 1]:
							end -= 1
							
					# search for smaller
					elif num[start] + num[end] > negate: 
						end -= 1
						
					# search for bigger
					else: 
						start += 1

		return result
	

s = Solution()				
print s.threeSum([-2,0,1,1,2])
		
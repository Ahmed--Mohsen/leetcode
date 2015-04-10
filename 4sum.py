from collections import defaultdict

class Solution:
	# @return a list of lists of length 4, [[val1,val2,val3]]
	def fourSum(self, num, target):
		n = len(num)
		result = set()
		
		#base case
		if len(num) < 4:
			return []
		
		# holds the pairs idexes that will sum to the key
		two_sums = defaultdict(list) 
		for i in range(n-1):
			for j in range(i+1, n):
				two_sums[num[i]+num[j]].append((i,j))
		
		# treat the problem as a 2-sum one
		for two_sum in two_sums.keys():
			remaining = target - two_sum
			if remaining in two_sums: # 4-sum exist
				for pair_1 in two_sums[two_sum]:
					for pair_2 in two_sums[remaining]:
						full_pair_indxs = set([pair_1[0], pair_1[1], pair_2[0], pair_2[1]])
						if len(full_pair_indxs) == 4: # no duplicates
							full_pair = tuple(sorted([num[ind] for ind in  full_pair_indxs]))
							result.add(full_pair)
			
		return [list(sums) for sums in result]
		
		
		
	#######################################################################	
		
	# caused TLE	
	# @return a list of lists of length 3, [[val1,val2,val3]]
	def fourSum_old(self, num, target):
		#base case
		if len(num) < 4:
			return []
		
		num.sort()
		result = []
		
		for i in range(len(num) - 3):
			if num[i] > target:
				break
			if i > 0 and num[i] == num[i-1]: #check duplicates
				continue
			for j in range(i+1, len(num) - 2):
				if num[i] + num[j] > target:
					break
				if j > i+1 and num[j] == num[j-1]:
					continue
				start = j + 1
				end = len(num) - 1
				while start < end:
					sum = num[i] + num[j] + num[start] + num[end]
					if sum == target: #found it
						result.append([num[i], num[j], num[start], num[end]])
						start += 1
						end -= 1
						while start < end and num[start] == num[start - 1]:
							start += 1
						
						while start < end and num[end] == num[end + 1]:
							end -= 1
					elif sum > target: #search for smaller
						end -= 1
					else:
						start += 1
				
		return result		



s = Solution()				
print s.fourSum([1, 0, -1, 0, -2, 2], 0)
		
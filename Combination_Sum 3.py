"""

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Ensure that numbers within the set are sorted in ascending order.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]

"""

class Solution:
	
	# @param {integer} k
	# @param {integer} n
	# @return {integer[][]}
	def combinationSum3(self, k, target):
		result = []
		candidates = [i for i in range(1,10)]
		self.combinationSumHelper(candidates, 0, target, 0, k,[], result)
		return result
	
	
	def combinationSumHelper(self, candidates, start, target, steps, target_steps, combination, result):
		# base case we reached the target
		if target == 0 and steps == target_steps: 
			result.append(list(combination))
			return
		
		# try the next candidates
		for i in range(start, len(candidates)):
			new_target = target - candidates[i]
			
			# can lead to new combination
			if new_target >= 0 and steps < target_steps: 
				combination.append(candidates[i])
				self.combinationSumHelper(candidates, i+1, new_target, steps + 1, target_steps, combination, result) # recurse
				combination.pop() # backtrack
				
			# no way to get to the target from this start casue candidates are sorted
			else: 
				break
				
				
s = Solution()
print s.combinationSum3(3, 9)
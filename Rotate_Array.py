class Solution:
	# @param nums, a list of integer
	# @param k, num of steps
	# @return nothing, please modify the nums list in-place.
	def rotate(self, nums, k):
		n = len(nums)
		k = k % n  #for k > n
		self.reverse(nums, 0, n - 1)	
		self.reverse(nums, 0, k - 1)
		self.reverse(nums, k, n - 1)

	# reverse the array from start to end positions
	# @param nums, a list of integer to be reversed
	# @param start, the starting position to start reversing
	# @param end, the ending position to start reversing
	def reverse(self, nums, start, end):
		i = start
		j = end
		while i < j:
			nums[i], nums[j] = nums[j], nums[i]
			i += 1
			j -= 1


s = Solution()
x = [1,2,3,4,5,6,7,8,9,10]
s.rotate(x, 3)
print x



		
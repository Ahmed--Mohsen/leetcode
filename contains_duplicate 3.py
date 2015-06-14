import sys

class Solution:
	# @param {integer[]} nums
	# @param {integer} k
	# @param {integer} t
	# @return {boolean}
	def containsNearbyAlmostDuplicate(self, nums, k, t):
		n = len(nums)
		
		# base case
		if k <  1 or t < 0:
			return False
		
		# a sliding window of size k (i and j is at most k)
		window = {}
		
		for i in range(n):
			# get the rescaled value for current num (handle -ve)
			rescaled = self.num_hash(nums[i])
			
			# map this rescaled num to a bucket (t+1) buckets (handle t=0)
 			bucket = self.bucket_key(nums[i], t)
			
			# check prev, same and next buckets
			for key in (bucket-1, bucket, bucket+1):
				if key in window and abs(window[key] - rescaled) <= t:
					return True
			
			# keep window size to max of k
			if len(window) >= k:
				# remove the element that is k steps from current num
				prev_k_bucket = self.bucket_key(nums[i-k], t)
				window.pop(prev_k_bucket, None)
			
			# add current element to its bucket
			window[bucket] = rescaled
		
		# no solution found
		return False
	
	# rescale each num to start from int.min
	def num_hash(self, num):
		min_int = - sys.maxsize - 1
		return num - min_int
	
	# map num to one of buckets of size t+1
	def bucket_key(self, num, t):
		return self.num_hash(num) / (t+1)

s = Solution()
print s.containsNearbyAlmostDuplicate([1,2,3],1,1)
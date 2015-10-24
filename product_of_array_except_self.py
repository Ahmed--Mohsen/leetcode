class Solution(object):
	
	"""
	:type nums: List[int]
	:rtype: List[int]
	"""
	def productExceptSelf(self, nums):
		n = len(nums)
		
		# base case
		if n in (0,1):
			return nums
			
		# the idea is to have 2 arrays and then the 
		# result would be the multiplication of each 
		# element
		# arr1: {              1,         a[0],    a[0]*a[1],    a[0]*a[1]*a[2],  }
		# arr2: { a[1]*a[2]*a[3],    a[2]*a[3],         a[3],                 1,  }
		
		result = [1] * n
		
		# build arr1
		product = 1
		for i in range(n):
			result[i] *= product
			product *= nums[i]
		
		# build arr2
		product = 1
		for i in range(n-1, -1, -1):
			result[i] *= product
			product *= nums[i]
		
		return result


s = Solution()
print s.productExceptSelf([1,2,3,4])
		
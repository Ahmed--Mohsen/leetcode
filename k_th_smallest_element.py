import random

class Solution():
	
	def rank(self, array, left, right, rank):
		pivot = array[random.randint(left, right)]
		
		# partition based on pivot and return left end
		left_end = self.partition(array, left, right, pivot)
		
		left_size = left_end - left + 1
		if left_size == rank + 1:
			return pivot
		elif left_size > rank:
			return self.rank(array, left, left_end, rank)
		else:
			return self.rank(array, left_end + 1, right, rank - left_size)
		
	def partition(self, array, left, right, pivot):
		while left <= right:
			while left <= right and array[left] <= pivot:
				left += 1
			while left <= right and array[right] > pivot:
				right -= 1
			if left < right:
				self.swap(array, left, right)
		return left - 1 
	
	def swap(self, array, i, j):
		temp = array[i]
		array[i] = array[j]
		array[j] = temp


s = Solution()
arr = [3,6,2,1,7,5]
#print s.partition(arr,0, len(arr)-1, 3 )
print arr
arr.sort()
print arr, arr[2]
print s.rank(arr,0,len(arr)-1,2)

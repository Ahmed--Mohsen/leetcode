class Solution:
	# @param A, a list of integers
	# @return an integer
	def trap(self, A):
		n = len(A)
		if n == 0:
			return 0
			
		trapped = 0
		left = 0; right = n -1
		max_left = 0; max_right = 0
		while left <= right:
			max_left = max(max_left, A[left])
			max_right = max(max_right, A[right])
			
			if max_left < max_right: #fill left
				trapped += max_left - A[left] 
				left += 1
			else: #fill right
				trapped += max_right - A[right]
				right -= 1
				
		return trapped
		
		
############################ Another Solution (DP) ############################
class Solution:
	# @param A, a list of integers
	# @return an integer
	def trap(self, A):
		n = len(A)
		if n == 0:
			return 0
			
		trapped = 0
		
		#move left to right
		ltr = [0]*n
		ltr[0] = A[0]
		for i in range(1, n):
			ltr[i] = max(ltr[i-1], A[i])
		
		#move right to left
		rtl = [0]*n
		rtl[n-1] = A[n-1]
		for i in range(n-2,-1,-1):
			rtl[i] = max(rtl[i+1], A[i])
		
		#calc trapped water
		for i in range(n):
			trapped += min(ltr[i], rtl[i]) - A[i]
				
		return trapped

		


s = Solution()
#print s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
#print s.trap([4,2,3])
print s.trap([4,2,0,3,2,5])
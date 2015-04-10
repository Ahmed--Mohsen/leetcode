class Solution:
	# @return a string
	def minWindow(self, S, T):
		s_len = len(S)
		t_len = len(T)
		
		
		#store count per char in t
		need_to_find = [0] * 256 #assuming all chars belong to ASCII
		for i in range(t_len):
			need_to_find[ord(T[i])] += 1
		
		#chars count found in s so far
		has_found = [0] * 256
		
		count = 0 #total count of chars in S that are already in T
		min_window_len = float("inf")
		min_window_start = 0; min_window_end = 0
		start = 0; end = 0
		
		while start < s_len and end < s_len:
			current = ord(S[end])
			if need_to_find[current] == 0: #not in T ... skip
				end += 1
				continue
			
			has_found[current] += 1
			
			if has_found[current] <= need_to_find[current]:
				count += 1
			
			
			#window constrain is met
			if count == t_len:
				#advance start as far right as possible
				while need_to_find[ord(S[start])] == 0 or (has_found[ord(S[start])] > need_to_find[ord(S[start])]):
					if has_found[ord(S[start])] > need_to_find[ord(S[start])]:
						has_found[ord(S[start])] -= 1
					#has_found[ord(S[start])] = max(0, has_found[ord(S[start])] - 1)
					start += 1
				
					
				window_len = end - start + 1
				if window_len < min_window_len:
					min_window_start = start
					min_window_end = end
					min_window_len = window_len
					
			end += 1
		if count == t_len:
			return S[min_window_start: min_window_end + 1]
		else: #not found
			return ""
		


s = Solution()		
print s.minWindow("ADOBECODEBANC", "XABC")
#print s.minWindow("acbbaca", "aba")
			
			
			
			
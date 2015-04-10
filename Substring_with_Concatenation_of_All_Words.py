class Solution:
	# @param S, a string
	# @param L, a list of string
	# @return a list of integer
	def findSubstring(self, S, L):
		words = set(L)
		word_len = len(L[0])
		num_of_words = len(L)
		word_count = {}
		for word in words:
			word_count[word] = L.count(word)
		valid_len = num_of_words * word_len
		
		starting_indexes = [] 
		
		i = 0
		while i + valid_len - 1  < len(S):
			current_word_count = {}
			j = 0
			while j < num_of_words:
				word = S[i+(j*word_len):i+(j*word_len)+word_len]
				if not word in words:
					break
				else:
					current_word_count[word] = current_word_count.get(word, 0) + 1
					if current_word_count[word] > word_count[word]:
						break
				j += 1
				
			if j == num_of_words:
				starting_indexes.append(i)
				
			i += 1
			
		return starting_indexes


s = Solution()
print s.findSubstring("barfoothefoobarman", ["foo", "bar"])
"""

Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

"""

class Solution:
	# @param s, a string
	# @param dict, a set of string
	# @return a list of strings
	def wordBreak(self, s, dict):
		if len(dict) == 0:
			return []
		
		self.dict = dict
		self.memo = {}
		result = []
		return self.wordBreakHelper(s)

	
	def wordBreakHelper(self, s):
		
		# use memo first if available
		if s in self.memo:
			return self.memo[s]
		
		words = []
		
		# check if the whole word belongs to the dict
		if s in self.dict:
			words.append(s)
			
			
		# try all breaking points for s
		for i in range(1, len(s)+1):
			left_word = s[:i]
			rigth_word = s[i:]
			
			if left_word in self.dict:
				
				# continue with rest
				sub_words = self.wordBreakHelper(rigth_word) 
				for word in sub_words:
					words.append(left_word+" "+word)
					
		self.memo[s] = words
		return words
		

############################################################################
##############################Another Solution##############################
############################################################################
class Solution:
	# @param s, a string
	# @param dict, a set of string
	# @return a list of strings
	def wordBreak(self, s, dict):
		if len(dict) == 0:
			return []
		
		self.dict = dict
		result = []
		memo = [True] * (len(s)+1)
		self.wordBreakHelper(s,0, [],result, memo)
		sentences = []
		for sentence in result:
			sentences.append(" ".join(sentence))
		return sentences
	
	def wordBreakHelper(self, s, start, sentence, result, memo):
		if start == len(s): #result found
			result.append(list(sentence))
			return True
		
		for end in range(start+1, len(s)+1):
			word = s[start:end]
			if word in self.dict and memo[end] == True:
				sentence.append(word) #add this word
				before_size = len(result)
				can_break = self.wordBreakHelper(s, end, sentence, result, memo) #continue with rest
				after_size = len(result)
				cant_break = (after_size == before_size)
				if cant_break:
					memo[end] = False
				sentence.pop() #backtrack

		return False


		
s = Solution()
ss = set()
ss.update(["cat", "cats", "and", "sand", "dog"]) 
print s.wordBreak("catsanddog", ss)
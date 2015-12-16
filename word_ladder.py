"""

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.

"""

class Solution:
	
	# @param start, a string
	# @param end, a string
	# @param dict, a set of string
	# @return an integer
	def ladderLength(self, start, end, dict):
		
		# base case
		if len(dict) == 0:
			return
		
		allChars = [chr(i) for i in range(ord('a'), ord('z') + 1)]
		
		wordQueue = []
		distanceQueue = []
		
		wordQueue.append(start)
		distanceQueue.append(1)
		dict.remove(start)
		
		while wordQueue:
			word = wordQueue.pop(0)
			distance = distanceQueue.pop(0)
				
			# search for replaces
			wordChars = list(word)
			for i in range(len(word)):
				for char in allChars:
					newWord = word[:i] + char + word[i + 1:]
					
					# we are done not necessary in dict
					if newWord == end: 
						return distance + 1
				
					# check if this word is in dictionary
					if newWord in dict:
						dict.remove(newWord) # mark as visited
						wordQueue.append(newWord)
						distanceQueue.append(distance + 1)

		return 0
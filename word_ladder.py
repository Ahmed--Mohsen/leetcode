class Solution:
	# @param start, a string
	# @param end, a string
	# @param dict, a set of string
	# @return an integer
	def ladderLength(self, start, end, dict):
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
				
			#search for replaces
			wordChars = list(word)
			for i in range(len(word)):
				for char in allChars:
					newWord = word[:i] + char + word[i + 1:]
					
					if newWord == end: #we are done not necessary in dict
						return distance + 1
				
					#check if this word is in dictionary
					if newWord in dict:
						dict.remove(newWord) #mark as visited
						wordQueue.append(newWord)
						distanceQueue.append(distance + 1)

		return 0
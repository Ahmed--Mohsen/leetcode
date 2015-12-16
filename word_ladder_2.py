"""

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
All words have the same length.
All words contain only lowercase alphabetic characters.


"""

from collections import deque
from collections import defaultdict

class Solution:
	# @param start, a string
	# @param end, a string
	# @param dict, a set of string
	# @return a list of lists of string
	def findLadders(self, start, end, dict):
		if len(dict) == 0 or start == end:
			return
		
		allChars = [chr(i) for i in range(ord('a'), ord('z') + 1)]
		
		wordQueue = deque([])			# BFS queue
		visited = set()		 				# hold nodes been visited in current level
		to_be_visited = set()			# holds nodes that will be visited in the next level	       
		parents = defaultdict(set)	# keep track of the the ancestors of a given word 
		found = False							# if true means we reached the end word no need to continue
		
		wordQueue.append(start)
		visited.add(start)
		dict.add(start)
		result = []
		
		# perform bfs in level order paradigm
		while wordQueue and not(found):

			# remove nodes that have been visited before
			# from the dictionary (to prevent loops)
			for next_word in wordQueue: 
				dict.remove(next_word)
			to_be_visited.clear()
				
			# visit all nodes in current level	
			level_len = len(wordQueue)
			for l in range(level_len):
				word = wordQueue.popleft()
				
				#search for replaces
				for i in range(len(word)):
					for char in allChars:
						if char == word[i]:
							continue
						newWord = word[:i] + char + word[i + 1:]

						if newWord == end: # search will be terminated (min path found)
							found = True
							parents[newWord].add(word)
						else: # check visiting the new node
							if newWord in dict:  # add link
								parents[newWord].add(word)
								if not newWord in to_be_visited: # visit the node
									wordQueue.append(newWord)
									to_be_visited.add(newWord)
									
								
		self.find_paths(end, start, [], result, parents)
		return result

	def find_paths(self, current, end, path, result, parents):
		# add the current node in the path reversely
		path.append(current)
		
		# reached the end
		if current == end: 
			found_path = list(path)
			found_path.reverse()
			result.append(found_path)
			
		# move up the tree
		for parent in parents[current]:
			self.find_paths(parent, end, path, result, parents)
		
		# backtrack
		path.pop(-1)
		

		
		
s = Solution()
print s.findLadders("hit", "cog", set(["hot","dot","dog","lot","log"]))
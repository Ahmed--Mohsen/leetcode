class Node:
	def __init__(self, word):
		self.val = word
		self.neighbors = []


class Solution:
	# @param start, a string
	# @param end, a string
	# @param dict, a set of string
	# @return a list of lists of string
	def findLadders(self, start, end, dict):
		node = self.build_graph(start, end, dict)
		print self.traverse_graph(node,end, [])
		
	def traverse_graph(self, root,end , path):
		if root == None:
			return path
		
		path.append(root.val)

		for neighbor in root.neighbors:
			if neighbor.val == end:
				path.append(end)
				print path
			else:
				#return path
				self.traverse_graph(neighbor,end, path)
		
	def build_graph(self, start, end, dict):
		if len(dict) == 0:
			return None
		
		allChars = [chr(i) for i in range(ord('a'), ord('z') + 1)]
		
		wordQueue = []
		
		startNode = Node(start)
		endNode = Node(end)
		wordQueue.append(startNode)
		if start in dict:
			dict.remove(start)
		if end in dict:
			dict.remove(end)
		
		while wordQueue:
			currentNode = wordQueue.pop(0)
			word = currentNode.val
				
			#search for replaces
			for i in range(len(word)):
				for char in allChars:
					newWord = word[:i] + char + word[i + 1:]
					
					if newWord == end: #we are done not necessary in dict
						currentNode.neighbors.append(endNode)
				
					#check if this word is in dictionary
					if newWord in dict:
						dict.remove(newWord) #mark as visited
						newNode = Node(newWord)
						currentNode.neighbors.append(newNode)
						wordQueue.append(newNode)

		return startNode

s = Solution()
s.findLadders("hit", "cog", set(["hot","dot","dog","lot","log"]))
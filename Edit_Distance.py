"""

Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character

"""

class Solution:
	# @return an integer
	def minDistance(self, word1, word2):
		# distance[i][j] = min operations to convert word1[0..i - 1] to word2[0..j - 1]
		distance = [[0]*(len(word2)+1) for i in range (len(word1)+1)]
		
		#base case if the other string is of len 0 then 
		#min distance is the len of the other one
		for i in range(len(distance)):
			distance[i][0] = i
		for j in range(len(distance[0])):
			distance[0][j] = j
		
		for i in range(1, len(distance)):
			for j in range(1, len(distance[0])):
				
				#if word1[i]==word2[j], then the distance of i and j is the previous i and j
				if word1[i-1] == word2[j-1]:
					distance[i][j] = distance[i-1][j-1]
				else: #take min of replace, insert or delete a char
					#insert char => distance[i-1][j] (match word1 at i-1 to word2 at j)
					#remove char => distance[i][j-1] (insert char at word2)
					#replace char => distance[i-1][j-1] (add one step to prev i and j)
					distance[i][j] = 1 + min(distance[i-1][j], min(distance[i][j-1], distance[i-1][j-1]))

		return distance[len(word1)][len(word2)]
		

s = Solution()
print s.minDistance("ab", "bc")
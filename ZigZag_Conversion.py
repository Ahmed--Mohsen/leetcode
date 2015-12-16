"""

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

"""

class Solution:
	
	# @return a string
	def convert(self, s, nRows):
		buffers = [ [] for i in range(nRows)]
		
		i = 0
		n = len(s)
		while i < n:
			
			#move down
			j = 0
			while i < n and j < nRows:
				buffers[j].append(s[i])
				j += 1
				i += 1
			
			#move up
			j = nRows - 2
			while i < n and j > 0:
				buffers[j].append(s[i])
				j -= 1
				i += 1
		
		#print the concatenation of all buffers
		for index in range(1, len(buffers)):
			buffers[0].extend(buffers[index])
		return "".join(buffers[0])
	
	
s = Solution()
print s.convert("PAYPALISHIRING", 3)
			